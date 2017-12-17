import re


def whitespace(string):
    return re.sub("[\s]", "", string)


def from_array(array, value):
    try:
        array.remove(value)
    except ValueError:
        pass
