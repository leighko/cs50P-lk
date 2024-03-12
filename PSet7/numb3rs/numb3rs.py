"""
implement a function called validate that expects an IPv4 address as input 
as a str and then returns True or False, respectively, if that input is a 
valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you’re welcome to modify main 
and/or implement other functions as you see fit, but you may not import 
any other libraries. You’re welcome, but not required, to use re and/or sys.

Either before or after you implement validate in numb3rs.py, additionally 
implement, in a file called test_numb3rs.py, two or more functions that 
collectively test your implementation of validate thoroughly, each of whose 
names should begin with test_ so that you can execute your tests.
"""

import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip: str) -> bool:
    if matches := re.search(r"^((?:[12])?[0-9]?[0-9]).((?:[12])?[0-9]?[0-9]).((?:[12])?[0-9]?[0-9]).((?:[12])?[0-9]?[0-9])$", ip):
        g1, g2, g3, g4 = matches.group(1,2,3,4)
        if int(g1) > 255 or int(g2) > 255 or int(g3) > 255 or int(g4) > 255:
            return False
        return True
    return False


if __name__ == "__main__":
    main()