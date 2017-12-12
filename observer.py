import re


class Observer:
    def execute(self, command):
        if command[-1:] == "=":
            print("Executing")
        else:
            print("Calling add and executing")
            self.add(command)

    def add(self, equation):
        split = equation.split("=")
        if re.match("^[a-zA-Z]+\([a-zA-Z]\)$", split[0]):
            print("This is a function")
        elif re.match("^[a-zA-Z]+$", split[0]):
            print("This is a variable")
        else:
            print("You did not give a valid variable/function name.")
