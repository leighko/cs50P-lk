"""
implement a function called count that expects a line of text as 
input as a str and returns, as an int, the number of times that 
“um” appears in that text, case-insensitively, as a word unto 
itself, not as a substring of some other word. For instance, given 
text like hello, um, world, the function should return 1. Given 
text like yummy, though, the function should return 0.

Structure um.py as follows, wherein you’re welcome to modify main 
and/or implement other functions as you see fit, but you may not 
import any other libraries. You’re welcome, but not required, to 
use re and/or sys.

Either before or after you implement count in um.py, additionally 
implement, in a file called test_um.py, three or more functions 
that collectively test your implementation of count thoroughly, 
each of whose names should begin with test_ so that you can 
execute your tests.
"""

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s: str) -> int:
    all_matches = re.findall(r"\w?um\w?", s, re.IGNORECASE)
    count_ums = 0
    for match in all_matches:
        if match.lower() == "um":
            count_ums += 1
    return count_ums
                    

if __name__ == "__main__":
    main()