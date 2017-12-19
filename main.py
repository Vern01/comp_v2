#!/usr/bin/env python3
import readline

import remove
import validate
from maths import Math
from memory import Memory


def main():
    memory = Memory()
    math = Math(memory)
    while 42:
        command = input("> ")
        if command == "exit":
            break
        command = remove.whitespace(command)
        command = command.lower()
        validate.equation(command)
        if command.endswith('?'):
            math.calc(command)
        else:
            memory.add_command(command)


if __name__ == '__main__':
    main()
