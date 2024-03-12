"""
implement a program that prompts the user for their date of birth in 
YYYY-MM-DD format and then sings prints how old they are in minutes, 
rounded to the nearest integer, using English words instead of numerals, 
just like the song from Rent, without any and between words. Since a user 
might not know the time at which they were born, assume, for simplicity, 
that the user was born at midnight (i.e., 00:00:00) on that date. And 
assume that the current time is also midnight. In other words, even if 
the user runs the program at noon, assume that it’s actually midnight, 
on the same date. Use datetime.date.today to get today’s date, per 
docs.python.org/3/library/datetime.html#datetime.date.today.

Structure your program per the below, not only with a main function but 
also with one or more other functions as well.

You’re welcome to import other (built-in) libraries, or any that are 
specified in the below hints. Exit via sys.exit if the user does not 
input a date in YYYY-MM-DD format. Ensure that your program will not 
raise any exceptions.

Either before or after you implement seasons.py, additionally implement, 
in a file called test_seasons.py, one or more functions that test your 
implementation of any functions besides main in seasons.py thoroughly, each 
of whose names should begin with test_ so that you can execute your tests.
"""

from datetime import date
import inflect
import operator
import re
import sys



def main():
    user_input = input("Date of Birth: ")
    valid_input = is_date_input_valid(user_input)
    minutes_int = years_to_minutes(valid_input)
    minutes_in_words = nums_to_words(minutes_int)
    print(f"{minutes_in_words} minutes.")
    

def is_date_input_valid(s: str) -> date:
    try:
        year, month, day = s.split("-")
        parsed_date = date(int(year), int(month), int(day))
        return parsed_date
    except:
        sys.exit("Incorrect date input.")


def years_to_minutes(valid_date):
    result = operator.__sub__(date.today(), valid_date)
    minutes = result.days * 24 * 60
    return minutes


def nums_to_words(mins):
    p = inflect.engine()
    words = p.number_to_words(mins, andword=" ")
    return words.capitalize()


if __name__ == "__main__":
    main()