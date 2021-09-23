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
        f = open(str_file, "r")
        self.__spec = json.loads(f.read())
        f.close()

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

    def make_function_get(self, path) -> str:
        str_get = self.__spec['paths'][path].get('get', '')
        if (0 < len(str_get)):
            str_function =  "\tdef {name}(self, {path_parameters}):\n"
            str_function += "\t\t\"\"\"{desciption}\n"
            str_function += "{param_decription}"
            str_function += "\t\t\"\"\"\n"
            str_function += "\t\treturn \"OK\"\n\n"

            func_name = self.build_function_name(path)
            func_name += "_get"

            str_params = "name1 : TODO_type, name2 : TODO_type"

            str_desciption = "TODO:path_description"

            return str_function.format(name = func_name, path_parameters = str_params, desciption = str_desciption)
        else:
            return ""

    def make_function_put(self, path) -> str:
        str_get = self.__spec['paths'][path].get('put', '')
        if (0 < len(str_get)):
            str_function =  "\tdef {name}(self, {path_parameters}):\n"
            str_function += "\t\t\"\"\"{desciption}\n"
            str_function += "{param_decription}"
            str_function += "\t\t\"\"\"\n"
            str_function += "\t\treturn \"OK\"\n\n"

            func_name = self.build_function_name(path)
            func_name += "_put"

            str_params = "name1 : TODO_type, name2 : TODO_type"

            str_desciption = "TODO:path_description"

            return str_function.format(name = func_name, path_parameters = str_params, desciption = str_desciption)
        else:
            return ""

    def make_function_post(self, path) -> str:
        str_get = self.__spec['paths'][path].get('post', '')
        if (0 < len(str_get)):
            str_function =  "\tdef {name}(self, {path_parameters}):\n"
            str_function += "\t\t\"\"\"{path_desciption}\n"
            str_function += "{param_decription}\n"
            str_function += "\t\t\"\"\"\n"
            str_function += "\t\treturn \"OK\"\n\n"

            func_name = self.build_function_name(path)
            func_name += "_post"

            str_path_parameters_format = "{name} : {type}"
            str_path_parameters = ""
            
            str_parmeter_description_format = "@param[{direction}] {name} - {type} {decription}"
            str_parmeter_description = ""

            # Ex: path "/measurement/consumable/{consumable_uuid}"
            # remove /{consumable_uuid}
            i_pos = path.find("/{")
            if (-1 != i_pos):
                # get the parameter info from the parameters list
                list_params = self.get_path_parameters(path, 'post')
            else:
                # get the parameter info from the requestBody 
                list_params = self.get_path_request_parameters(path, 'post')

            i_count = len(list_params)
            i_n = 1

            for param in list_params:
                str_parmeter_description += "\t\t"
                str_parmeter_description += str_parmeter_description_format.format(
                                                direction=param['direction'],
                                                name=param['name'],
                                                type=param['type'],
                                                decription=param['decription'])
                if (i_n < i_count):
                    str_parmeter_description += "\n"

                str_path_parameters += str_path_parameters_format.format(
                                                name=param['name'],
                                                type=param['type'])
                if (i_n < i_count):
                    str_path_parameters += ", "
                
                i_n += 1

            str_path_desciption = "TODO:path_description"

            rtn_str = str_function.format(
                        name = func_name,
                        path_parameters = str_path_parameters,
                        param_decription = str_parmeter_description,
                        path_desciption = str_path_desciption)
            return rtn_str
        else:
            return ""


    def get_path_parameters(self, path, verb) -> list:
        """
        
        """
        str_ref = self.__spec['paths'][path][verb].get('parameters', '')
        print("str_ref: %s" % str_ref)
        # TODO - BUILD list_params from parameters

        list_params = [
            {
                "name": "consumable_uuid",
                "direction": "in",
                    "type": str_type,
                    "decription": str_description
            }
        ]

        return list_params


    def get_path_request_parameters(self, path, verb) -> list:
        """
        
        """
        list_params = []

        dict_requestbody = self.__spec['paths'][path][verb].get('requestBody', '')
        value = dict_requestbody.get('$ref')
        if ("" != value):
            # Ex requestBody "$ref": "#/components/requestBodies/body_script_json"
            str_path = value[2:] # drop the leading #/
        else:
            str_path = value

        # append the rest of the expected path
        dict_description = self.get_object_from_path(str_path)
        str_description = dict_description.get('description', '')
        
        str_schema = str_path + "/content/application*json/schema"
        dict_schema = self.get_object_from_path(str_schema)
        str_type = dict_schema.get('type', '')

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
        except e:
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
        """
        str_func = spec.make_function_get(path)
        if (0 < len(str_func)):
            print(str_func)
            f.write(str_func)
        
        str_func = spec.make_function_put(path)
        if (0 < len(str_func)):
            print(str_func)
            f.write(str_func)
        """
        
        str_func = spec.make_function_post(path)
        if (0 < len(str_func)):
            print(str_func)
            f.write(str_func)

    f.close()

if __name__ == '__main__':
    main()

