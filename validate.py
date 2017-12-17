import re

import log
import remove


def equation(string):
    non_valid = re.findall("[^a-z()\d*/%+\-=^\[\];,]+", string)
    if non_valid:
        log.exceptions(non_valid, "Syntax error: ")
    if string.count('=') != 1:
        log.exception("Make sure that there is only one '=' sign.")
    invalid_operations = re.findall("[*/+\-%][*/+\-%]+", string)
    invalid_operations = set(invalid_operations)
    remove.from_array(invalid_operations, "**")
    if invalid_operations:
        log.exceptions(invalid_operations, "Invalid operation: ")
    if string.count('(') != string.count(')') or string.count('[') != string.count(']'):
        log.exception("Your parenthesis or brackets do not match up.")
    if re.search("\(\)|\[\]"):
        log.exception("Parenthesis and brackets are not allowed to be empty.")

