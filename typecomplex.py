import re
import factory


class TypeComplex:
    def __init__(self, complex):
        self.value = self.complex_convert(complex)

    def complex_convert(self, complex):
        complex_split = re.split("[+-]", complex)
        i_dic = {}
        for part in complex_split:
            if 'i' in part:
                pos = part.index('i')
                if pos - 1 == '*':
                    part = part[:pos - 1] + part[pos:]

            else:
                i_dic['0'] = factory.int_rational(part)