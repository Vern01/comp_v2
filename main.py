#!/usr/bin/env python3
import readline

from observer import Observer
import remove


def main():
    ob = Observer()
    while 42:
        command = input("> ")
        print(command)
        if command == "exit":
            break
        command = remove.whitespace(command)
        if "=" not in command:
            print("This is an invalid command. You need to use the '=' sign.")
        elif command.endswith("?"):
            ob.execute(command[:-1])
        else:
            ob.add(command)


if __name__ == '__main__':
    main()
