#!/usr/bin/env python3

"""
@brief generate_dbus_functions.py

Reads the openAPISpec.json file and creates the dbus functions
"""
 
import json
import os
from functools import reduce  # forward compatibility for Python 3
import operator


class Payload(object):
    def __init__(self, str_file):
        self.__str_function =  "\tdef {name}(self{path_parameters}):\n"
        self.__str_function += "\t\t\"\"\"{path_desciption}\n"
        self.__str_function += "{param_decription}\n"
        self.__str_function += "\t\t\"\"\"\n"
        self.__str_function += "\t\treturn \"OK\"\n\n"

        self.__str_path_parameters_format = "{name} : {type}"
            
        self.__str_parameter_description_format = "@param[{direction}] {name} - {type} {decription}"
        self.clear_func_vars()

        f = open(str_file, "r")
        self.__spec = json.loads(f.read())
        f.close()

    def clear_func_vars(self):
        self.__str_func_name = ""
        self.__str_path_parameters = ""
        self.__str_parameter_description = ""
        self.__str_path_desciption = ""



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
            str_type = self.get_dbus_data_type(param['type'])

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
                                            type=str_type)
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

            rtn_str = self.__str_function.format(
                        name = self.__str_func_name,
                        path_parameters = self.__str_path_parameters,
                        param_decription = self.__str_parameter_description,
                        path_desciption = self.__str_path_desciption)
            return rtn_str
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

            rtn_str = self.__str_function.format(
                        name = self.__str_func_name,
                        path_parameters = self.__str_path_parameters,
                        param_decription = self.__str_parameter_description,
                        path_desciption = self.__str_path_desciption)
            return rtn_str
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

            rtn_str = self.__str_function.format(
                        name = self.__str_func_name,
                        path_parameters = self.__str_path_parameters,
                        param_decription = self.__str_parameter_description,
                        path_desciption = self.__str_path_desciption)
            return rtn_str
        else:
            return ""


    def get_path_parameters(self, path) -> list:
        """
        
        """
        list_params = []
        str_name = ""
        str_type = ""
        str_description = ""

        list_parameters = self.__spec['paths'][path].get('parameters', '')
        
        try:
            for dict_parameter in list_parameters:
                str_name = dict_parameter.get('name', '')
                str_description = dict_parameter.get('description', '')
                
                dict_schema = dict_parameter.get('schema', '')
                str_type = dict_schema.get('type', '')
                str_type = self.get_dbus_data_type(str_type)
        except Exception as e:
            print(e)
            return list_params

        list_params = [
            {
                "name": str_name,
                "direction": "in",
                "type": str_type,
                "decription": str_description
            }
        ]

        return list_params


    def get_dbus_data_type(self, str_json_type : str) -> str:
        if ("string" == str_json_type.lower()):
            return "str"
        else:
            print("TODO - define a DBus type for JSON type: %s" % str_json_type)
            return str_json_type


    def get_path_request_parameters(self, path, verb) -> list:
        """
        
        """
        list_params = []
        str_type = ""
        str_description = ""

        dict_requestbody = self.__spec['paths'][path][verb].get('requestBody', '')
        if (0 == len(dict_requestbody)):
            return list_params

        value = dict_requestbody.get('$ref')
        if (None != value):
            # Ex requestBody "$ref": "#/components/requestBodies/body_script_json"
            str_path = value[2:] # drop the leading #/
        else:
            str_path = value

        try:
            # append the rest of the expected path
            dict_description = self.get_object_from_path(str_path)
            str_description = dict_description.get('description', '')
            
            str_schema = str_path + "/content/application*json/schema"
            dict_schema = self.get_object_from_path(str_schema)
            str_type = dict_schema.get('type', '')
        except Exception as e:
            print(e)
            return list_params

        list_params = [
            {
                "name": "body",
                "direction": "in",
                "type": str_type,
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
    spec = Payload(str_path_json)
    paths = spec.get_paths()

    str_path_class = dir_path + '/../CAnalyzerX.py'

    f = open(str_path_class, "w")
    f.write("#!/usr/bin/env python3\n")
    f.write("\"\"\"\n")
    f.write("@breif CAnalyzer.py\n")
    f.write("\n")
    f.write("Purpose: DBus service interface for the analyzer app.\n")
    f.write("\"\"\"\n")
    f.write("\n")
    f.write("class CAnalyzerX():\n")

    for path in paths:
        str_func = spec.make_function_get(path)
        if (0 < len(str_func)):
            print(str_func)
            f.write(str_func)
        
        str_func = spec.make_function_put(path)
        if (0 < len(str_func)):
            print(str_func)
            f.write(str_func)

        str_func = spec.make_function_post(path)
        if (0 < len(str_func)):
            print(str_func)
            f.write(str_func)

    f.close()

if __name__ == '__main__':
    main()

