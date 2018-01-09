import maths

from typerational import TypeRational


def parentheses(string):
    if '(' in string:
        first_close = string.index(')')
        last_open = string.rindex('(', end=first_close)
        enclosed = string[last_open + 1 : first_close]
        string = string[:last_open + 1] + maths.solve(enclosed) + string[first_close:]
        # if not re.fullmatch("[+-]", string[last_open - 1]) and not re.fullmatch("[+-]", string[first_close + 1]):
    return string


def add(type1, type2):
    if isinstance(type1, type2):
        func = type(type1)
    else:
        return TypeRational(type1.value + type2.value)
    return func(type1.value + type2.value)


def subtract(type1, type2):
    if isinstance(type1, type2):
        func = type(type1)
    else:
        return TypeRational(type1.value - type2.value)
    return func(type1.value - type2.value)
