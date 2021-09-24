#!/usr/bin/env python3

"""
@brief generate_dbus_functions.py

Reads the openAPISpec.json file and creates the dbus functions
"""
 
import json
import os
from functools import reduce  # forward compatibility for Python 3
import operator

from dbus_next_data_types import class_dbus_next_types


class Payload(object):
    def __init__(self, str_file):
        self.__str_function =  "\t{func_decorator}\n"
        self.__str_function +=  "\tdef {func_name}(self{path_parameters}) -> {func_return_type}:\n"
        self.__str_function += "\t\t\"\"\"{path_desciption}\n"
        self.__str_function += "{param_decription}\n"
        self.__str_function += "\t\t\"\"\"\n"
        self.__str_function += "\t\treturn {default_return}\n\n"

        self.__str_path_parameters_format = "{name} : {type}"
            
        self.__str_parameter_description_format = "@param[{direction}] {name} - {type} {decription}"
        self.clear_func_vars()

        f = open(str_file, "r")
        self.__spec = json.loads(f.read())
        f.close()

    def clear_func_vars(self):
        self.__str_func_decorator = "@method()"
        self.__str_func_name = ""
        self.__str_path_parameters = ""
        self.__str_parameter_description = ""
        self.__str_path_desciption = ""
        self.__str_func_return_type = "'s'"
        self.__default_return = "str({\"response\":\"not implimented\"})"


    def get_function_body(self) -> str:
        rtn_str = self.__str_function.format(
                    func_decorator = self.__str_func_decorator,
                    func_name = self.__str_func_name,
                    path_parameters = self.__str_path_parameters,
                    param_decription = self.__str_parameter_description,
                    path_desciption = self.__str_path_desciption,
                    func_return_type = self.__str_func_return_type,
                    default_return = self.__default_return)
        return rtn_str


    def get_paths(self) -> dict:
        return self.__spec['paths']

    def build_function_name(self, str_path) -> str:
        # Ex: path "/measurement/consumable/{consumable_uuid}"
        # drop the leading '/'
        str_fun = str_path[1:]

        # remove /{consumable_uuid}
        i_pos = str_fun.find("/{")
        if (-1 != i_pos):
            str_fun = str_fun[:i_pos]

        # subitute '/' with '_'
        str_name = str_fun.replace("/", "_")

        return str_name

    def set_parameter_descriptions(self, list_params):
        i_count = len(list_params)
        i_n = 1

        for param in list_params:
            self.__str_parameter_description += "\t\t"
            str_dbus_type = class_dbus_next_types.get_dbus_data_type(param['type'])

            self.__str_parameter_description += self.__str_parameter_description_format.format(
                                            direction=param['direction'],
                                            name=param['name'],
                                            type=param['type'],
                                            decription=param['decription'])
            if (i_n < i_count):
                self.__str_parameter_description += "\n"

            if (1 == i_n):
                self.__str_path_parameters += ", "
            self.__str_path_parameters += self.__str_path_parameters_format.format(
                                            name=param['name'],
                                            type=str_dbus_type)
            if (i_n < i_count):
                self.__str_path_parameters += ", "
            
            i_n += 1


    def make_function_get(self, path) -> str:
        self.clear_func_vars()

        dict_verb = self.__spec['paths'][path].get('get', '')
        if (0 < len(dict_verb)):
            self.__str_func_name = self.build_function_name(path)
            self.__str_func_name += "_get"

            self.__str_path_desciption = dict_verb['description']

            list_params = self.get_path_request_parameters(path, 'get')
            self.set_parameter_descriptions(list_params)

            return self.get_function_body()

        else:
            return ""


    def make_function_put(self, path) -> str:
        self.clear_func_vars()

        dict_verb = self.__spec['paths'][path].get('put', '')
        if (0 < len(dict_verb)):
            self.__str_func_name = self.build_function_name(path)
            self.__str_func_name += "_put"

            self.__str_path_desciption = dict_verb['description']

            list_params = self.get_path_request_parameters(path, 'put')
            self.set_parameter_descriptions(list_params)

            return self.get_function_body()

        else:
            return ""


    def make_function_post(self, path) -> str:
        self.clear_func_vars()

        dict_verb = self.__spec['paths'][path].get('post', '')
        if (0 < len(dict_verb)):
            self.__str_func_name = self.build_function_name(path)
            self.__str_func_name += "_post"

            self.__str_path_desciption = dict_verb['description']

            # Ex: path "/measurement/consumable/{consumable_uuid}"
            # remove /{consumable_uuid}
            i_pos = path.find("/{")
            if (-1 != i_pos):
                # get the parameter info from the parameters list
                list_params = self.get_path_parameters(path)
            else:
                # get the parameter info from the requestBody 
                list_params = self.get_path_request_parameters(path, 'post')

            self.set_parameter_descriptions(list_params)

            return self.get_function_body()

        else:
            return ""


    def get_path_parameters(self, path) -> list:
        """
        
        """
        list_params = []
        str_name = ""
        str_json_type = ""
        str_description = ""

        list_parameters = self.__spec['paths'][path].get('parameters', '')
        
        try:
            for dict_parameter in list_parameters:
                str_name = dict_parameter.get('name', '')
                str_description = dict_parameter.get('description', '')
                
                dict_schema = dict_parameter.get('schema', '')
                str_json_type = dict_schema.get('type', '')
        except Exception as e:
            print(e)
            return list_params

        list_params = [
            {
                "name": str_name,
                "direction": "in",
                "type": str_json_type,
                "decription": str_description
            }
        ]

        return list_params


    def get_path_request_parameters(self, path, verb) -> list:
        """
        
        """
        list_params = []
        str_description = ""

        dict_requestbody = self.__spec['paths'][path][verb].get('requestBody', '')
        if (0 == len(dict_requestbody)):
            return list_params

        try:
            value = dict_requestbody.get('$ref')
            if (None != value):
                # Ex requestBody "$ref": "#/components/requestBodies/body_script_json"
                # drop the leading #/
                str_component_name = value[2:]
                dict_requestbody = self.get_object_from_path(str_component_name)

                str_schema = str_component_name + "/content/application*json/schema"
                dict_schema = self.get_object_from_path(str_schema)
                str_description = dict_requestbody.get('description', '')
                str_json_type = dict_schema.get('type', '')
            else:
                dict_schema = dict_requestbody['content']['application/json']['schema']
                str_description = dict_schema.get('description', '')
                str_json_type = dict_schema.get('type', '')
        except Exception as e:
            print(e)
            return list_params

        list_params = [
            {
                "name": "body",
                "direction": "in",
                "type": str_json_type,
                "decription": str_description
            }
        ]

        return list_params

    def get_object_from_path(self, str_path : str) -> dict:
        """ Parse the str_path and get the object at that end point
        """
        mapList = str_path.split("/")

        for index, item in enumerate(mapList):
            if (-1 != item.find("*")):
                fixed_item = item.replace("*", "/")
                mapList[index] = fixed_item

        try:
            dict_rtn = reduce(operator.getitem, mapList, self.__spec)
        except Exception as e:
            print(e)
            dict_rtn = {}

        return dict_rtn




def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    str_path_json = dir_path + '/openAPISpec.json'

    str_path_class = dir_path + '/../CAnalyzerBase.py'
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

    spec = Payload(str_path_json)
    paths = spec.get_paths()

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
    main()

