from typeinterger import TypeInteger
from typerational import TypeRational


def int_rational(value):
    if int(value) == float(value):
        return TypeInteger(value)
    else:
        return TypeRational(value)