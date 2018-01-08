#!/usr/bin/env python3
import readline

import remove
import validate
from maths import Math
from memory import Memory


def main():
    memory = Memory()
    math = Math(memory)
    memory.set_math(math)
    while 42:
        command = input("> ")
        if command == "exit":
            break
        command = remove.whitespace(command)
        command = command.lower()
        validate.equation(command)
        if command.endswith('?'):
            math.calc(command[:-1])
        else:
            memory.add_command(command)
        print(memory.array)


if __name__ == '__main__':
    main()
