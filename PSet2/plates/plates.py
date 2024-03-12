"""
In Massachusetts, home to Harvard University, it’s possible 
to request a vanity license plate for your car, with your 
choice of letters and numbers instead of random ones. Among 
the requirements, though, are:

    “All vanity plates must start with at least two letters.”
    “… vanity plates may contain a maximum of 6 characters 
        (letters or numbers) and a minimum of 2 characters.”
    “Numbers cannot be used in the middle of a plate; they 
        must come at the end. For example, AAA222 would be an 
        acceptable … vanity plate; AAA22A would not be acceptable. 
        The first number used cannot be a ‘0’.”
    “No periods, spaces, or punctuation marks are allowed.”

In plates.py, implement a program that prompts the user for a 
vanity plate and then output Valid if meets all of the requirements 
or Invalid if it does not. Assume that any letters in the user’s 
input will be uppercase. Structure your program per the below, 
wherein is_valid returns True if s meets all requirements and False 
if it does not. Assume that s will be a str. You’re welcome to 
implement additional functions for is_valid to call (e.g., one 
function per requirement).
"""

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool: 
    if not first_two_num(s):
        return False
    if not plate_length(s):
        return False
    if not punct_check(s):
        return False
    if not num_check(s):
        return False
    else:
        return True
    

# WORKING 
# Making sure first two characters are alpha
def first_two_num(first_two):
    if first_two[0].isnumeric() or first_two[1].isnumeric():
        return False
    else:
        return True


# WORKING
# Making sure whole string is between 2 and 6 characters
def plate_length(whole_plate):
    if len(whole_plate) < 2 or len(whole_plate) > 6:
        return False

    return True


# WORKING
# Making sure no punctuation in string
def punct_check(pl):
    for char in pl:
        if not char.isalnum():
            return False
    return True


# WORKING
# Making sure numbers are in appropriate indexes
def num_check(plate_num):
    first_num = ""
    for char in plate_num[2:]:
        if char.isnumeric():
            if first_num == "":
                first_num = char  
            if first_num == "0":
                return False
        else:
            if first_num != "":
                return False
    return True
            

if __name__ == "__main__":
    main()