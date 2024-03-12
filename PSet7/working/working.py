"""
implement a function called convert that expects a str in either 
of the 12-hour formats below and returns the corresponding str in 
24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be 
capitalized (with no periods therein) and that there will be a space 
before each. Assume that these times are representative of actual 
times, not necessarily 9:00 AM and 5:00 PM specifically.

    9:00 AM to 5:00 PM
    9 AM to 5 PM

Raise a ValueError instead if the input to convert is not in either 
of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, 
etc.). But do not assume that someone’s hours will start ante meridiem 
and end post meridiem; someone might work late and even long hours 
(e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main 
and/or implement other functions as you see fit, but you may not import 
any other libraries. You’re welcome, but not required, to use re and/or sys.

Either before or after you implement convert in working.py, additionally 
implement, in a file called test_working.py, three or more functions that 
collectively test your implementation of convert thoroughly, each of whose 
names should begin with test_ so that you can execute your tests.
"""

import re


def main():
    output = convert(input("Hours: "))
    if output:
        print(output)


def convert(s: str) -> str:
    # time = re.search(r"^((?:.+)?(?:[1])?\d(?:.+)[aAmM|aPmM]?)\sto\s((?:.+)?(?:[1])?\d(?:.+)[aAmM|pPmM]?)$", s, re.IGNORECASE)
    start_time, end_time = s.strip().split(" to ")
    s_time, s_am_pm = start_time.split(" ")
    e_time, e_am_pm = end_time.split(" ")

    if ":" not in s_time:
        s_time = f"{s_time}:00"
    if ":" not in e_time:
        e_time = f"{e_time}:00"
    
    s_hour, s_minute = s_time.split(":")
    s_num_hour = int(s_hour)
    s_num_min = int(s_minute)

    e_hour, e_minute = e_time.split(":")
    e_num_hour = int(e_hour)
    e_num_min = int(e_minute)

    if s_num_hour > 12 or e_num_hour > 12 or s_num_min > 59 or e_num_min > 59:
        raise ValueError
    
    # if s_am_pm.lower() != "am" or s_am_pm.lower() != "pm":
    #     raise ValueError
    
    # if e_am_pm.lower() != "am" or e_am_pm.lower() != "pm":
    #     raise ValueError

    else:
        start_time_formatted = reformat(s_num_hour, s_num_min, s_am_pm.lower())
        end_time_formatted = reformat(e_num_hour, e_num_min, e_am_pm.lower())
        return f"{start_time_formatted} to {end_time_formatted}"


def reformat(hour: int, minute: int, am_pm: str) -> str:
    if am_pm == 'pm' and hour != 12:
        hour += 12
    elif am_pm == "am" and hour == 12:
        hour = 0
    
    final_output = f"{hour:02}:{minute:02}"
    return final_output


if __name__ == "__main__":
    main()