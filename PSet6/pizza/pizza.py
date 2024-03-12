"""
implement a program that expects exactly one command-line argument, the 
name (or path) of a CSV file in Pinocchio’s format, and outputs a table 
formatted as ASCII art using tabulate, a package on PyPI at 
pypi.org/project/tabulate. Format the table using the library’s grid format. 
If the user does not specify exactly one command-line argument, or if the 
specified file’s name does not end in .csv, or if the specified file does 
not exist, the program should instead exit via sys.exit.
"""

import csv
import sys
import tabulate


def main():
    try:
        user_input = sys.argv
        output = find_file(user_input[1])
        print(tabulate.tabulate(output[1:], headers=output[0], tablefmt="grid"))
    except:
        input_error_checker(user_input)
        

def input_error_checker(cla_input: list) -> None:
    if len(cla_input) < 2:
        sys.exit("Too few arguments")
    elif len(cla_input) > 2:
        sys.exit("Too many arguments")
    elif not cla_input[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    elif FileNotFoundError:
        sys.exit("File does not exist")


def find_file(cla: str) -> list:
    path = f"/Users/lk/Desktop/coder/personalprojects/cs50P/pizza/{cla}"
    with open(path) as csvfile:
        menu_list = []
        for row in csv.reader(csvfile):
            menu_list.append(row)
    return menu_list

            


if __name__ == "__main__":
    main()