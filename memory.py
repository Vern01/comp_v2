import re

import log
import validate
from functiontype import FunctionType


class Memory:
    def __init__(self):
        self.array = {'i': "i", 'vara': "42", "test(": FunctionType("test(x)=x+1".split('='))}
        self.math = None

    def set_math(self, math):
        self.math = math

    def set_values(self,command, ignore=""):
        variables = re.findall("(?<=[*/+\-%(=])[a-z]+(?=[*/+\-%)^])|[a-z]+(?=[*/+\-%^=]|\Z)", command)
        variables = set(variables)
        print("_______________________Variables Replace________________________\n", variables)
        for var in variables:
            print(var)
            if var != ignore:
                value = self.array.get(var, None)
                if not value:
                    log.exception("Undefined variable: " + var)
                command = command.replace(var, value)
        functions = re.findall("(?<=[*/+\-%(])[a-z]+\(.+\)(?=[*/+\-%)]|)|[a-z]+\(.+\)(?=[*/+\-%])", command)
        functions = set(functions)
        print("_______________________Functions Replace________________________\n", functions)
        for func in functions:
            funct = self.array.get(func[:func.index('(') + 1])
            if not funct:
                log.exception("Function is not defined, " + func)
            value = funct.param(re.search("(?<=\().+(?=\))", func).group(0))
            command = command.replace(func, value)
        return command

    def set_vars_func(self, command, ignore=""):
        command = self.math.calc(command, ignore)
        return command

    def add_command(self, command):
        command_split = command.split('=')
        if re.fullmatch("[a-z]+\(.+\)", command_split[0]):
            print("I am creating a function type.")
            param = re.search("(?<=\()[a-z]+(?=\))", command_split[0]).group(0)
            validate.var_func_names(command, param)
            command_split[1] = self.set_vars_func(command_split[1], param)
            self.array[re.match("[a-z]+\(?", command_split[0]).group(0)] = FunctionType(command_split)
        else:
            print("I am assigning this to a variable")
            if command_split[0] == "i":
                log.exception("Variable name is not allowed to be 'i'/'I'.")
            validate.var_func_names(command)
            self.array[command_split[0]] = self.set_vars_func(command_split[1])
        print(self.array)

    def query(self, value):
        return self.array[value]
