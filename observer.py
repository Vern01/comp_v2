import re

from functiontype import FunctionType
import validate


class Observer:
    def __init__(self):
        self.array = {
            'func(': FunctionType("x + 1", "x")
        }

    def __get_value(self, var, param_value):
        if not param_value:
            return self.array[var]
        return self.array[var].param(param_value)

    def __replace_types(self, equation, param):
        equation = equation.lower()
        variables = re.findall("[a-z]+|[a-z]+\(\d\)", equation)
        for variable in variables:
            var = re.match("[a-z]+\(?", variable).group(0)
            param_value = re.search("(?<=\()\d+(?=\))", variable)
            if param_value:
                param_value = param_value.group(0)
            if var != param:
                if var in self.array:
                    equation = equation.replace(var, self.__get_value(variable, param_value))
                else:
                    print("'" + var + "' has not been defined.")
                    raise Exception
        return equation

    def execute(self, command):
        if command[-1:] == "=":
            print("Executing")
        else:
            print("Calling add and executing")
            self.add(command)

    def add(self, equation):
            equation = equation.lower()
            split = equation.split("=")
        # try:
            if len(split) > 2:
                print("You cannot have more than one '=' sign.")
                raise Exception
            if len(split[1]) < 1:
                print("A variable cannot be set equal to blank.")
                raise Exception
            if re.match("^[a-z]+\([a-z]\)$", split[0]):
                print("This is a function")
                param = re.search("(?<=\()[a-z]+(?=\))", split[0]).group(0)
                validate.equation(split[1], param)
                pure_str = self.__replace_types(split[1], param)
                self.array[re.match("[a-z]+\(", split[0]).group(0)] = FunctionType(pure_str, param)
            elif re.match("^[a-z]+$", split[0]):
                validate.equation(split[1])
                print("This is a rational number or imaginary or matrix.")
            else:
                print("You did not give a valid variable/function name.")
            print(self.array)
        # except Exception:
        #     print("Fix the error and try again. Use the up arrow key to get last command.")
