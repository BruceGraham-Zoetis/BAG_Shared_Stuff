#!/usr/bin/env python3

"""
@file print_utility.py

$ pip3 install pycups

VMWare Linux
===================
CUPS - open source printing system
Originally standing for Common Unix Printing System.
CUPS allows a computer to act as a print server.

Uniform Resource Identifier (URI)


# Setup the printer
# -p Specifies the name of the printer to add.
# -E Enables the destination and accepts jobs.
# -v Sets the device-uri attribute of the print queue.
$ lpadmin -p HPOfficejetPro -E -v cups-brf:/


# list drivers and related information.

$ lpinfo -v
serial serial:/dev/ttyS0?baud=115200
network https
file cups-brf:/
network beh
network http
network lpd
network socket
network ipps
network ipp
direct hp
direct hpfax

# display the status of a printer
$ lpstat -p
lpstat: No destinations added.

# lists available printers
$ lpstat -d
no system default destination

# print queue status
$ lpq
lpq: Error - no default destination available.


"""

import cups
import inspect
from os.path import exists


class class_vetscan_print_utility():
    """! The vetscan network control class.
    """

    def __init__(self, user_name = "", user_password = ""):
        """! The class_vetscan_print_utility class initializer.
        @param -none-
        @return  An instance of the initialized class class_vetscan_print_utility.
        """

        # TODO - verify dependant services are installed
        # 

        cups_connection = cups.Connection()
        
        self.__debug = False # True: enable printing when an error occurs
        self.__user_name = user_name
        self.__user_password = user_password
        self.__str_default_printer_name = cups_connection.getDefault()
        self.__print_options = {"page-left":"30", "cpi":"12"} # TODO Add function to get and set options
        self.__dict_printers = {}
        self.__print_job_id = -1

        # Set server to connect to.
        cups.setServer("localhost")
 
        # Set user to connect as.
        if ("" != self.__user_name):
            cups.setUser(self.__user_name)

        # Set password callback function.
        # This Python function will be called when a password is required.
        # It must take one string parameter (the password prompt) and it
        # must return a string (the password).
        # To abort the operation it may return the empty string ('').
        cups.setPasswordCB(self.password_callback)

        self.update_known_printers()

        

    def debug_on(self):
        self.__debug = True

    def debug_off(self):
        self.__debug = False


    def password_callback(self, not_used):
        if (self.__debug and "" == self.__user_password): print("Warning: user_password is blank")
        return self.__user_password


    def update_known_printers(self):
        cups_connection = cups.Connection()
        printers = cups_connection.getPrinters()

        # determine the currently selected printer
        self.__str_default_printer_name = cups_connection.getDefault()
        self.__dict_printers = {}

        # add each known printer
        for str_printer_uri in printers:
            self.__dict_printers[str_printer_uri] = printers[str_printer_uri]["device-uri"]
            if (0 == len(self.__str_default_printer_name)):
                self.__default_printer = str_printer_uri


    def get_printers_name_list(self) -> list:
        if (0 == len(self.__dict_printers)):
            self.update_known_printers()

        list_uri = []

        for key in self.__dict_printers.keys():
            list_uri.append(key)

        return list_uri


    def get_printer_info_dict(self) -> dict:
        self.update_known_printers()
        return self.__dict_printers


    def is_valid_printer_name(self, str_default_printer_name : str) -> bool:
        list_names = self.get_printers_name_list()

        for device_name in list_names:
            if (device_name == str_default_printer_name):
                return True
        
        return False


    def set_default_printer(self, str_default_printer_name : str) -> bool:
        """! Set the default printer to use by given printer name.
        If a default system printer has been set, and you want to use it, then you can use 'default'.
        The name must be a printer name. Use get_printers_name_list() to get configured system printer names.

        Example:
            set_default_printer('default')
            set_default_printer('HPSuperjet')

        @param[in] str str_default_printer_name = Printer name
        """

        try:
            cups_connection = cups.Connection()

            if ('default' == str_default_printer_name):
                str_default = cups_connection.getDefault()
                if (None != str_default):
                    str_default_printer_name = str_default
                    cups_connection.setDefault(str_default_printer_name)
                    return True
                else:
                    if (self.__debug):
                        print("ERROR: No default printer in CUPS (see http://localhost:631)")
                    return False
            else:
                b_valid = self.is_valid_printer_name(str_default_printer_name)
                if (not b_valid):
                    if (self.__debug):
                        print("ERROR: No printer named '%s' in CUPS (see http://localhost:631)" % str_default_printer_name)
                    return False
                else:
                    return True
        except Exception as e:
            if (self.__debug):
                print("ERROR %s %s" % (inspect.currentframe().f_code.co_name, str_default_printer_name))
                print(e)
            return False


    def get_default_printer(self) -> str:
        cups_connection = cups.Connection()
        return cups_connection.getDefault()


    def print_file(self, str_path_file_name : str) -> int:	
        """! Print a file, given a path and file name. Blocks until file is printed.

        Example:
            print_file("./test_data_files/test_print_file.pdf")

        @param[in] str_path_file_name = path and file name of a printable file.

        @returns int - not 0, print job id
        @returns int - 0, failed
        """

        try:
            cups_connection = cups.Connection()
            if (0 == len(self.__default_printer)):
                self.__default_printer = cups_connection.getDefault()
            
            if (0 == len(self.str_default_printer_name)):
                if (self.__debug):
                    print("ERROR: print_file() default printer not set")
                return 0

            file_exists = exists(str_path_file_name)
            if (not file_exists):
                if (self.__debug):
                    print("ERROR: print_file() File not found %s" % (str_path_file_name))
                return 0

            if (self.__debug):
                print("print_file(%s) to the default printer %s" % (str_path_file_name, self.__str_default_printer_name))
            self.__print_job_id = cups_connection.printFile(self.__str_default_printer_name, str_path_file_name, " ", self.__print_options)
            return self.__print_job_id

        except Exception as e:
            if (self.__debug):
                print("ERROR %s %s" % (inspect.currentframe().f_code.co_name, str_path_file_name))
                print(e)
            return 0


    def add_printer_device(self, str_printer_name : str, str_printer_uri : str) -> bool:
        """! Add the ptiner by name and device URI.

            @param[in] str str_printer_name - printer name
            @param[in] str str_printer_uri - printer URI
        """
        
        try:
            cups_connection = cups.Connection()
            cups_connection.setPrinterDevice(str_printer_name, str_printer_uri)
        except Exception as e:
            if (self.__debug):
                print("ERROR %s %s %s" % (inspect.currentframe().f_code.co_name, str_printer_name, str_printer_uri))
                print(e)
            return 0
            

    def enable_printer(self, str_printer_uri : str):
        try:
            cups_connection = cups.Connection()
            cups_connection.enablePrinter(str_printer_uri)
        except (cups.IPPError) as e:
            if (self.__debug):
                print(inspect.currentframe().f_code.co_name)
                print(e)
            return None
 
    def disable_printer(self, str_printer_uri : str):
        try:
            cups_connection = cups.Connection()
            cups_connection.disablePrinter(str_printer_uri)
        except (cups.IPPError) as e:
            if (self.__debug):
                print(inspect.currentframe().f_code.co_name)
                print(e)
            return None

    def has_print_completed(self, id_print_job):
        try:
            cups_connection = cups.Connection()
            jobs = cups_connection.getJobs(first_job_id =id_print_job, requested_attributes=["job-id"])

            if (0 == len(jobs)):
                # no print jobs in process
                return True

            for job_id in jobs:
                if (job_id == id_print_job):
                    return False
                else:
                    return True
        except (cups.IPPError) as e:
            if (self.__debug):
                print(inspect.currentframe().f_code.co_name)
                print(e)
            return False

    def get_jobs(self):
        try:
            cups_connection = cups.Connection()
            jobs = cups_connection.getJobs(requested_attributes=["job-id", 'printer-uri', 'time-at-creation', 'time-at-processing', 'time-at-completed', 'job-state', 'job-state-reasons'])
            return jobs
        except (cups.IPPError) as e:
            if (self.__debug):
                print(inspect.currentframe().f_code.co_name)
                print(e)
            return None
 
 
    def cancel_job(self, job_id):
        try:
            cups_connection = cups.Connection()
            cups_connection.cancelJob(int(job_id))
        except (cups.IPPError) as e:
            if (self.__debug):
                print(inspect.currentframe().f_code.co_name)
                print(e)
            return None
 
    def cancel_all_jobs(self, str_printer_uri : str):
        jobs = self.get_jobs()
        try:
            cups_connection = cups.Connection()
            for job_id in jobs:
                if jobs[job_id]['printer-uri'].endswith(str_printer_uri):
                    cups_connection.cancelJob(int(job_id))
        except (cups.IPPError) as e:
            if (self.__debug):
                print(inspect.currentframe().f_code.co_name)
                print(e)
            return None


if __name__ == '__main__':
    print_util = class_vetscan_print_utility()
    print_util.debug_on()

    dict_printers_info = print_util.get_printer_info_dict()
    print("printer info:")
    print(dict_printers_info)
    print("")

    list_printer_uri = print_util.get_printers_name_list()
    print("printers name list:")
    print(list_printer_uri)
    print("")

    str_default = print_util.get_default_printer()
    print("default printer:")
    print(str_default)
    print("")

    # TODO Remove a printer and add a printer

    # add_printer_device()
    # enable_printer()
    # disable_printer()


    b_rtn = print_util.set_default_printer("bogus")
    if (b_rtn):
        print("ERROR: found bogus printer")

    b_rtn = print_util.set_default_printer(str_default)
    if (not b_rtn):
        print("ERROR: did not find printer: %s" % str_default)

    # TODO - print a pdf file



    #print_job_id = print_util.print_file("./test_data_files/test_text_file.txt")
    print_job_id = print_util.print_file("./test_data_files/enwik8.pmd")
    print("print_job_id: %d" % print_job_id)
    print("")

    print("Wait for printing to complete\n")
    while (not print_util.has_print_completed(print_job_id)):
        print(".", end="")
        #time.sleep(0.01)
    
    print("\nPrinting has completed")

