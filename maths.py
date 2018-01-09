def solve(equation):
    print("Needs to solve equation.")


class Math:
    def __init__(self, memory):
        self.memory = memory

    def calc(self, string, ignore=""):
        values = self.memory.set_values(string, ignore)
        return string
