"""
implement a program that:

    Expects the user to provide two command-line arguments:
        the name of an existing CSV file to read as input, whose columns 
            are assumed to be, in order, name and house, and
        the name of a new CSV to write as output, whose columns should be, 
            in order, first, last, and house.
    Converts that input to that output, splitting each name into a first 
        name and last name. Assume that each student will have both a first 
        name and last name.

If the user does not provide exactly two command-line arguments, or if 
the first cannot be read, the program should exit via sys.exit with an 
error message.
"""

import csv
import sys


def main():
    try:
        user_input = sys.argv
        read_file(user_input)
    except:
        error_checker(user_input)


def error_checker(cla_input: list) -> None:
    if len(cla_input) < 3:
        sys.exit("Too few command-line arguments")
    elif len(cla_input) > 3:
        sys.exit("Too many command-line arguments")
    elif FileNotFoundError:
        sys.exit(f"Could not read {cla_input[1]}")


def read_file(cla: list) -> None:
    file_1_path = f"/Users/lk/Desktop/coder/personalprojects/cs50P/scourgify/{cla[1]}"
    file_2_path = f"/Users/lk/Desktop/coder/personalprojects/cs50P/scourgify/{cla[2]}"

    with open(file_1_path) as file:
        reader = csv.DictReader(file)
        
        with open(file_2_path, "w", newline="") as new_file:
            fieldnames = ["first_name", "last_name", "house"]
            writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            writer.writeheader()
            
            for line in reader:
                last, first = line["name"].split(",")
                writer.writerow({"first_name": first, "last_name": last, "house": line["house"]})


if __name__ == "__main__":
    main()