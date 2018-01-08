import simplify


def solve(equation):
    print ("Needs to solve equation.")


class Math:
    def __init__(self, memory):
        self.memory = memory

    def calc(self, string, ignore=""):
        string = self.memory.set_values(string, ignore)
        print(string)
        if '=' in string:
            print("Move over everything from the right to the left.")
        # todo Get rid of all parentheses - Call self and remember to return.
        string = simplify.parentheses(string)
        # todo Write function to do all '*', '**', '/'
            # p.s Matrices cannot be divided.
        # todo Find types that can be added or subtracted together (ComputerV1)
        return string
