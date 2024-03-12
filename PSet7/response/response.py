"""
using either validator-collection or validators from PyPI, implement 
a program that prompts the user for an email address via input and 
then prints Valid or Invalid, respectively, if the input is a 
syntatically valid email address. You may not use re. And do not 
validate whether the email address’s domain name actually exists.
"""

import validator_collection


def main():
    print(validate_email(input("What's your email address? ")))


def validate_email(s):
    if email_address := validator_collection.checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"
    

if __name__ == "__main__":
    main()