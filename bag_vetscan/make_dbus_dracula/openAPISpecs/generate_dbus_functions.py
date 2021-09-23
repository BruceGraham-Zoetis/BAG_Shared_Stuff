#!/usr/bin/env python3

"""
@brief generate_dbus_functions.py

Reads the openAPISpec.json file and creates the dbus functions
"""
 
import json
import os


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

        # drop the trailing '/'
        str_fun = str_fun[:-1]

        # subitute '/' with '_'
        str_name = str_fun.replace("/", "_")

        return str_name

    def make_function_get(self, path) -> str:
        str_get = self.__spec['paths'][path].get('get', '')
        if (0 < len(str_get)):
            str_function =  "\tdef {name}(self, {params}):\n"
            str_function += "\t\t\"\"\"{desciption}\n"
            str_function += "\t\t@param[in] TODO:param_name - TODO:param_type TODO:param_decription\n"
            str_function += "\t\t\"\"\"\n"
            str_function += "\t\treturn \"OK\"\n\n"

            func_name = self.build_function_name(path)
            func_name += "_get"

            list_param = "name1 : TODO_type, name2 : TODO_type"

            str_desciption = "TODO:path_description"

            return str_function.format(name = func_name, params = list_param, desciption = str_desciption)
        else:
            return ""

    def make_function_put(self, path) -> str:
        str_get = self.__spec['paths'][path].get('put', '')
        if (0 < len(str_get)):
            str_function =  "\tdef {name}(self, {params}):\n"
            str_function += "\t\t\"\"\"{desciption}\n"
            str_function += "\t\t@param[in] TODO:param_name - TODO:param_type TODO:param_decription\n"
            str_function += "\t\t\"\"\"\n"
            str_function += "\t\treturn \"OK\"\n\n"

            func_name = self.build_function_name(path)
            func_name += "_put"

            list_param = "name1 : TODO_type, name2 : TODO_type"

            str_desciption = "TODO:path_description"

            return str_function.format(name = func_name, params = list_param, desciption = str_desciption)
        else:
            return ""

    def make_function_post(self, path) -> str:
        str_get = self.__spec['paths'][path].get('post', '')
        if (0 < len(str_get)):
            str_function =  "\tdef {name}(self, {params}):\n"
            str_function += "\t\t\"\"\"{desciption}\n"
            str_function += "\t\t@param[in] TODO:param_name - TODO:param_type TODO:param_decription\n"
            str_function += "\t\t\"\"\"\n"
            str_function += "\t\treturn \"OK\"\n\n"

            func_name = self.build_function_name(path)
            func_name += "_post"

            # Ex: path "/measurement/consumable/{consumable_uuid}"
            # remove /{consumable_uuid}
            i_pos = path.find("/{")
            if (-1 != i_pos):
                list_param = path[i_pos + 2 : -1]
                list_param += " : TODO_type"
            else:
                list_param = "name1 : TODO_type, name2 : TODO_type"

            str_desciption = "TODO:path_description"

            return str_function.format(name = func_name, params = list_param, desciption = str_desciption)
        else:
            return ""

    def get_end_point_requestbody(self, path, verb) -> dict:
        return self.__spec['paths'][path][verb].get('requestBody', '')


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


