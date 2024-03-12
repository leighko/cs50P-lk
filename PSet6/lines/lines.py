"""
implement a program that expects exactly one command-line argument, 
the name (or path) of a Python file, and outputs the number of lines 
of code in that file, excluding comments and blank lines. If the user 
does not specify exactly one command-line argument, or if the specified 
file’s name does not end in .py, or if the specified file does not exist, 
the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, 
is a comment. (A docstring should not be considered a comment.) Assume that 
any line that only contains whitespace is blank.
"""

import sys


def main():
    try:
        user_input = sys.argv
        loc = count_lines(user_input[1])
    except Exception as e:
        if type(e) is IndexError:
            print("Too few command-line arguments")
        elif len(user_input) > 2:
            print("Too many command-line arguments")
        elif user_input[1].endswith(".py") == False:
            print("Not a python file")
        elif type(e) is FileNotFoundError:
            print("File does not exist")
        sys.exit()
    print(loc)


def count_lines(cla: str) -> int:
    path = f"/Users/lk/Desktop/coder/personalprojects/cs50P/lines/{cla}"
    with open(path) as file:
        total_lines = 0
        for line in file.readlines():
            if line == "\n" or "#" in line:
                pass
            else:
                total_lines += 1
    return total_lines


if __name__ == "__main__":
    main()