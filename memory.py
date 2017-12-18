import re

import log


class Memory:
    def __init__(self):
        self.array = {'i': "i"}

    def __set_vars_func(self, command):
        variables = re.findall("(?<=[*/+\-%(])([a-z]+)(?=[*/+\-%)])|([a-z]+)(?=[*/+\-%]|\Z)", command)
        variables = set(variables)
        for var in variables:
            if not var.isalpha():
                log.exception("Invalid variable: " + var)
            value = self.array.get(var, None)
            if not value:
                log.exception("Undefined variable: " + var)
            command = command.replace(var, value)
        functions = re.findall("(?<=[*/+\-%(])([a-z]+\(.+\))(?=[*/+\-%)]|)|([a-z]+\(.+\))(?=[*/+\-%])", command)
        functions = set(functions)
        for func in functions:
            value = self.array.get(func[:func.index('(') + 1]).param(re.search("(?<=\().+(?=\))", func).group(0))
            command = command.replace(func, value)
        return command

    def add_command(self, command):
        command = command.split('=')
        pure_command = self.__set_vars_func(command[1])
        if re.fullmatch("[a-z]+\(.+\)", command[0]):
            print("Creating function type.")
            self.array[re.match("[a-z]+\(?", command[0])] = pure_command
        else:
            print("Checking which type.")

    def query(self, value):
        print("This is the query value.")
