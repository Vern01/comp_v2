import simplify


class FunctionType:
    def __init__(self, equation, param_letter):
        self.letter = param_letter
        self.equation = simplify.algebra_equation(equation)
        print("From FunctionType: eq= " + equation + "\nlet= " + param_letter)

    def __str__(self):
        return self.equation

    def param(self, value):
        return value.replace(self.letter, value)
