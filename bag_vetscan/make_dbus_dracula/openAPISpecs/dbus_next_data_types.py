#!/usr/bin/env python3
"""
@breif dbus_next_data_types.py

Purpose: functions for getting dbus_next data types for given types used in openAPISpec.json

https://python-dbus-next.readthedocs.io/en/latest/type-system/index.html

"""

import json


class class_dbus_next_types():
    def __init__(self):
        """
        static members only
        """
        pass

    @classmethod
    def get_dbus_data_type(cls, str_openapi_type : str) -> str:
        str_dbus_type = ""

        str_type = str_openapi_type.lower()

        if ("string" == str_type):
            str_dbus_type = "'s'"
        else:
            #print("TODO - define a DBus type for JSON type: %s" % str_openapi_type)
            str_dbus_type = "'a{ss}'"
            
        return str_dbus_type


    @classmethod
    def convert_openapi_type(cls, str_openapi_type : str) -> str:
        """ Convert a given openapi type to a dbus-next @method and @signals data types

        @param[in] str_openapi_type - string from the openAPISpec.json file

        @returns str - a dbus-next data type for @method and @signals
        """
        str_dbus_type = ""

        str_type = str_openapi_type.lower()

        if ("string" == str_type):
            # python type: str
            str_dbus_type = "'s'"

        elif ("number" == str_type): # integer or floating-point
            # python type: int or float
            str_dbus_type = "'s'"

        elif ("object" == str_type):
            # python type: dbus_next.Variant
            str_dbus_type = "'v'"

        elif ("array" == str_type):
            # python type: list
            str_dbus_type = "'a'"

        elif ("boolean" == str_type):
            # python type: bool
            str_dbus_type = "'b'"

        elif ("integer" == str_type):
            # python type: int
            str_dbus_type = "'i'"

            """
            TODO - Handle complex data types
            
            Ex:
            {
                'foo': Variant('s', 'bar'),
                'bat': Variant('x', -55),
                'a_list': Variant('as', ['hello', 'world'])
            }
            type: "'a{sv}'"

            Ex:
            [what1, what2]
            type: "'ss'"

            
            """

        else:
            """
            """
            #print("TODO - define a DBus type for JSON type: %s" % str_openapi_type)
            #str_dbus_type = "'a{ss}'"
            pass
            
        return str_dbus_type

    @classmethod
    def get_type_from_openapi_example(cls, str_dbus_type : str, str_example : str) -> str:
        print("\nget_type_from_openapi_example(%s, %s)" % (str_dbus_type, str_example))
        str_dbus_type = ""

        str_type = class_dbus_next_types.convert_openapi_type(str_example)
        if (0 != len(str_type)):
            str_dbus_type += str_type
        else:
            dict_from_str = json.loads(str_example)
            # array of dict entries - start
            str_dbus_type += "a{"

            for key in dict_from_str:
                # key type
                str_dbus_type += 's'

                # value type
                value = dict_from_str[key]

                if (isinstance(value, str)):
                    str_dbus_type += 's'

                elif (isinstance(value, int)):
                    str_dbus_type += 'i'

                elif (isinstance(value, list)):
                    str_dbus_type += '(a)'

                elif (isinstance(value, dict)):
                    str_dbus_type += '{a}'

                else:
                    print("ERROR: UNKNOWN TYPE:", value)
                    str_dbus_type += 's'

            # array of dict entries - end
            str_dbus_type += "}"

        return str_dbus_type

    @classmethod
    def convert_schema(cls, str_dbus_type : str, str_schema : str) -> str:
        print("\nconvert_schema(%s, %s)" % (str_dbus_type, str_schema))
        
        str_type = class_dbus_next_types.convert_openapi_type(str_schema)
        if (0 != len(str_type)):
            str_dbus_type += str_type
        else:
            dict_from_str = json.loads(str_schema)

            for key in dict_from_str:
                if ("type" == key):
                    str_type = class_dbus_next_types.convert_schema(str_dbus_type, dict_from_str[key])
                    str_dbus_type += str_type

        return str_dbus_type


if __name__ == '__main__':
    str_example = '{ "foo": "bar" }'
    str_type = class_dbus_next_types.get_type_from_openapi_example("", str_example)
    print("\tExpected: as")
    print("\tActual: ", str_type)
    print("")

    str_example = '{ "foo": 5 }'
    str_type = class_dbus_next_types.get_type_from_openapi_example("", str_example)
    print("\tExpected: a{su}")
    print("\tActual: ", str_type)
    print("")

    str_example = '{"list": ["one", "two", "three" ]}'
    str_type = class_dbus_next_types.get_type_from_openapi_example("", str_example)
    print("\tExpected: as")
    print("\tActual: ", str_type)
    print("")

    print("")

    str_schema = '{"type": "string", "description": "YYYY-MM-DD", "example": "2021-05-13"}'
    str_type = class_dbus_next_types.convert_schema("", str_schema)
    print("\tExpected: (su)")
    print("\tActual: ", str_type)
    print("")
