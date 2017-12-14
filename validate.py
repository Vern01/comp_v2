import re


def __findall_reg(regex, string, msg):
    array = re.findall(regex, string)
    if array:
        array = set(array)
        for element in array:
            print("'" + element + "', " + msg)
        raise Exception


def equation(eq, ignore):
    # Not valid character
    __findall_reg("[^\w()+\-*/%=;,\[\]^.\d]", eq, "is an invalid character.")
    # variables
    string = eq
    if ignore:
        string = eq.replace(ignore, "")
    __findall_reg("[^=+\-*/%a-zA-Z]+[a-zA-Z]+|[a-zA-Z]+[^=+\-*/%a-zA-Z\^]+", string, "is an invalid variable.")
    # Operators
    signs = re.findall("[+\-*/%][+\-*/%]+", eq)
    if signs and set(signs) != {'**'}:
        for invalid in signs:
            if invalid != "**":
                print("'" + invalid + "' invalid use of operators.")
            raise Exception
    if re.search("[*/+\-][=]|[=][*/+]|[*/+\-]$", eq):
        print("You are missing a value or you have one operator to many.")
        raise Exception
