import re


class FunctionType:
    def __init__(self, command):
        self.letter = re.search("(?<=\()[a-z]+(?=\))", command[0]).group(0)
        self.equation = command[1]
        print("From FunctionType: eq= " + self.equation + "\nlet= " + self.letter)

    def __str__(self):
        return self.equation

    def param(self, value):
        return self.equation.replace(self.letter, value)
