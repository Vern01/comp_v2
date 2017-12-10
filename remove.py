import re


def whitespace(string):
    return re.sub("[\s]", "", string)
