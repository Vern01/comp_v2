import re

from functiontype import FunctionType
import validate


class Observer:
    def __init__(self):
        self.function_array = []

    def __replace_vars(self, equation):
        print("hi")

    def execute(self, command):
        if command[-1:] == "=":
            print("Executing")
        else:
            print("Calling add and executing")
            self.add(command)

    def add(self, equation):
        split = equation.split("=")
        try:
            if len(split) > 2:
                print("You cannot have more than one '=' sign.")
                raise Exception
            if len(split[1]) < 1:
                print("A variable cannot be set equal to blank.")
                raise Exception
            self.__replace_vars(split[1])
            if re.match("^[a-zA-Z]+\([a-zA-Z]\)$", split[0]):
                print("This is a function")
                param = re.search("(?<=\()[a-zA-Z]+(?=\))", split[0]).group(0)
                validate.equation(split[1], param)
                self.function_array.append(FunctionType(split[1], param))
            elif re.match("^[a-zA-Z]+$", split[0]):
                validate.equation(split[1], None)
                print("This is a rational number or imaginary or matrix.")
            else:
                print("You did not give a valid variable/function name.")
        except Exception:
            print("Fix the error and try again. Use the up arrow key to get last command.")
