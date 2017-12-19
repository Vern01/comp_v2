import re

import log
import remove


def equation(string):
    non_valid = re.findall("[^a-z()\d*/%+\-=^\[\];,?]+", string)
    if non_valid:
        log.exceptions(non_valid, "Syntax error: ")
    if string.count('=') != 1:
        log.exception("Make sure that there is only one '=' sign.")
    invalid_operations = re.findall("[*/+\-%][*/+\-%]+", string)
    invalid_operations = set(invalid_operations)
    if "**" in invalid_operations:
        remove.from_array(invalid_operations, "**")
    if invalid_operations:
        log.exceptions(invalid_operations, "Invalid operation: ")
    if string.count('(') != string.count(')') or string.count('[') != string.count(']'):
        log.exception("Your parenthesis or brackets do not match up.")
    if re.search("\(\)|\[\]", string):
        log.exception("Parenthesis and brackets are not allowed to be empty.")


def var_func_names(string, ignore=""):
    print("var_func_names(string, ignore=""): ", string, " ,", ignore)
    regex = "[^*/+\-%^()=\[\];,." + ignore + "]+"
    values = re.findall(regex, string)
    for value in values:
        if not value.isalpha() and not re.match("[\d.]", value):
            log.exception("This is not a valid function or variable name: " + value)
