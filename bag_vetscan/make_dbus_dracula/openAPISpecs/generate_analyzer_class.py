#!/usr/bin/env python3

"""
@brief generate_analyzer_class.py
"""

import os
import json

class CParameter():
    def __init__(self):
        self.__str_name = ""         # Ex: 'consumable_uuid'
        self.__str_desciption = ""   # Ex: 'The UUID of the consumable'
        self.__str_openapi_type = "" # Ex: 'string'
        self.__str_dbus_type = ""    # Ex: 's'


class CFunction():
    def __init__(self):
        self.__path = ""             # Ex: /measurement/consumable/{consumable_uuid}
        self.__str_name = ""         # Ex: def measurement_consumable_post(self, consumable_uuid : 's') -> 's':
        self.__list_requestBody = "" # Ex: /components/requestBodies/body_script_json
        self.__list_parameters = ""  # Ex: 
        self.__responses = ""

    def build_function(str_path : str) -> str:
        # Ex:
        # def measurement_consumable_post(self, consumable_uuid : 's') -> 's':

        str_function =  "\t{func_decorator}\n"
        str_function +=  "\tdef {func_name}(self{path_parameters}) -> {func_return_type}:\n"
        str_function += "\t\t\"\"\"{path_desciption}\n"
        str_function += "{param_decription}\n"
        str_function += "\t\t\"\"\"\n"
        str_function += "\t\treturn {default_return}\n\n"



class COpenAPI_JSON():
    def __init__(self):
        self.__dict_spec = {}       # dictionary of the entire specification
        self.__dict_functions = {}  # dictionary of type CFunction

    def load_file(self, str_openapi_json_file_name : str) -> bool:
        f = open(str_openapi_json_file_name, "r")
        self.__dict_spec = json.loads(f.read())
        f.close()



        return True

    def generate_class(self, str_path_class) -> bool:
        f = open(str_path_class, "w")
        f.write("#!/usr/bin/env python3\n")
        f.write("\"\"\"\n")
        f.write("@breif CAnalyzerBase.py\n")
        f.write("\n")
        f.write("Purpose: DBus service interface for the analyzer app.\n")
        f.write("\n")
        f.write("Notes:\n")
        f.write("The parameters and return types must be type cast. For example: use 's' for str type.\n")
        f.write("See https://python-dbus-next.readthedocs.io/en/latest/type-system\n")
        f.write("\n")

        f.write("\"\"\"\n")
        f.write("\n")
        f.write("from dbus_next.service import (ServiceInterface, method)\n")
        f.write("\n")
        f.write("# ServiceInterface exports Methods: @method(), Properties: @property, Signals:@signal()\n")
        f.write("class CAnalyzerBase(ServiceInterface):\n")
        f.write("\tdef __init__(self, str_analyzer_name):\n")
        f.write("\t\tsuper().__init__(str_analyzer_name)\n")
        f.write("\n")

        paths = self.__dict_spec['paths']

        for path in paths:
            str_func = spec.make_function_get(path)
            if (0 < len(str_func)):
                #print(str_func)
                f.write(str_func)
            
            str_func = spec.make_function_put(path)
            if (0 < len(str_func)):
                #print(str_func)
                f.write(str_func)

            str_func = spec.make_function_post(path)
            if (0 < len(str_func)):
                #print(str_func)
                f.write(str_func)

        f.close()

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    str_openapi_json_file_name = dir_path + '/openAPISpec.json'
    str_path_class = dir_path + '/../CAnalyzerBase.py'

    JFile = COpenAPI_JSON()
    b_rtn = JFile.load_file(str_openapi_json_file_name)
    if (not b_rtn):
        print("ERROR: failed to load file")
        exit(1)

    b_rtn = JFile.generate_class(str_path_class)
    if (not b_rtn):
        print("ERROR: failed to generate class")
        exit(1)
    

    
