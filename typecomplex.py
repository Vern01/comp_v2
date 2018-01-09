import re

import factory
import simplify


class TypeComplex:
    def __init__(self, comp):
        self.value = self.complex_convert(comp)
        self.key_map = [1, 'i', -1, '-i']

    def complex_convert(self, comp):
        comp_split = re.findall("[+-]?[^+-]+", comp)
        i_dic = {}
        for part in comp_split:
            if 'i' in part:
                pos = part.index('i')
                if part[pos - 1] == '*':
                    part = part[:pos - 1] + part[pos:]
                    pos -= 1
                    print('Removing * for i: ', part)
                if pos == part.length - 1:
                    i_dic[1] = factory.int_rational(part[:pos])
                if part[pos + 1] == '^':
                    i_dic[int(part[pos + 2:])] += factory.int_rational(part[:pos])
            else:
                i_dic[0] += factory.int_rational(part)
        return self.simplify_complex(i_dic)

    def simplify_complex(self, i_dic):
        print(i_dic)
        for key, value in i_dic.items():
            if key > 1:
                if self.key_map[key % 4] == 1:
                    i_dic[0] = simplify.add(i_dic[0], i_dic[key])
                elif self.key_map[key % 4] == 'i':
                    i_dic[1] = simplify.add(i_dic[1], i_dic[key])
                elif self.key_map[key % 4] == -1:
                    i_dic[0] = simplify.subtract(i_dic[0], i_dic[key])
                elif self.key_map[key % 4] == '-i':
                    i_dic[1] = simplify.subtract(i_dic[1], i_dic[key])
                del i_dic[key]
        return i_dic

    def display(self):
        print(self.value[0].value + " " + self.value[1].value + "i")
