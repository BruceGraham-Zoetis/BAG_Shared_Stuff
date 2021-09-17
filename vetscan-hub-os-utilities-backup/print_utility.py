#!/usr/bin/env python3

"""
@file print_utility.py

@brief This class uses the CUPS.
CUPS - open source printing system
Originally standing for Common Unix Printing System.
CUPS allows a computer to act as a print server.


Printer Queue: A logical device name that is logically linked to a printer URI.
    Example: CUPS-BRF-Printer

Printer URI: Uniform Resource Identifier. 
    Example: serial:/dev/ttyS0

$ pip3 install pycups

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
        self.__str_printer_queue_name = cups_connection.getDefault()
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

        self.update_current_printer_queue_names()

        

    def debug_on(self):
        self.__debug = True

    def debug_off(self):
        self.__debug = False


    def password_callback(self, not_used):
        if (self.__debug and "" == self.__user_password): print("Warning: user_password is blank")
        return self.__user_password


    def update_current_printer_queue_names(self):
        cups_connection = cups.Connection()
        printers = cups_connection.getPrinters()

        # determine the currently selected printer
        self.__str_printer_queue_name = cups_connection.getDefault()
        self.__dict_printers = {}

        # add each known printer
        for str_printer_uri in printers:
            self.__dict_printers[str_printer_uri] = printers[str_printer_uri]["device-uri"]
            if (0 == len(self.__str_printer_queue_name)):
                self.__default_printer = str_printer_uri


    def get_printers_queue_name_list(self) -> list:
        """! Get a list of the system printer queue names.

        @param[in] None

        @return list of printer queue names
        """

        if (0 == len(self.__dict_printers)):
            self.update_current_printer_queue_names()

        list_uri = []

        for key in self.__dict_printers.keys():
            list_uri.append(key)

        return list_uri


    def get_current_printer_queue_info_dict(self) -> dict:
        """! Get a dictionary of the system printers.

        @param[in] None

        @return dictionary of the system printers
        """

        self.update_current_printer_queue_names()
        return self.__dict_printers


    def is_valid_printer_name(self, str_printer_queue_name : str) -> bool:
        list_names = self.get_printers_queue_name_list()

        for device_name in list_names:
            if (device_name == str_printer_queue_name):
                return True
        
        return False


    def set_default_printer(self, str_printer_queue_name : str) -> bool:
        """! Set the default printer to use by given printer's print queue name.
        
        The name must be a printer queue name that is already setup.
        
        Use get_printers_queue_name_list() to get configured system printer queue names.

        Example:
            set_default_printer('HPSuperjet')

        @param[in] str str_printer_queue_name = Printer name
        """

        try:
            cups_connection = cups.Connection()

            b_valid = self.is_valid_printer_name(str_printer_queue_name)
            if (not b_valid):
                if (self.__debug):
                    print("ERROR: No printer named '%s' in CUPS (see http://localhost:631)" % str_printer_queue_name)
                return False
            else:
                cups_connection.setDefault(str_printer_queue_name)
                # verify it got set to the default
                str_default = cups_connection.getDefault()
                if (str_default == str_printer_queue_name):
                    return True
                else:
                    return False
        except Exception as e:
            if (self.__debug):
                print("ERROR %s %s" % (inspect.currentframe().f_code.co_name, str_printer_queue_name))
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
            
            if (0 == len(self.str_printer_queue_name)):
                if (self.__debug):
                    print("ERROR: print_file() default printer not set")
                return 0

            file_exists = exists(str_path_file_name)
            if (not file_exists):
                if (self.__debug):
                    print("ERROR: print_file() File not found %s" % (str_path_file_name))
                return 0

            if (self.__debug):
                print("print_file(%s) to the default printer %s" % (str_path_file_name, self.__str_printer_queue_name))
            self.__print_job_id = cups_connection.printFile(self.__str_printer_queue_name, str_path_file_name, " ", self.__print_options)
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

    dict_printers_info = print_util.get_current_printer_queue_info_dict()
    print("printer info:")
    print(dict_printers_info)
    print("")

    list_printer_uri = print_util.get_printers_queue_name_list()
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

