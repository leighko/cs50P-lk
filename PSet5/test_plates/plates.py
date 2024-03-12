"""
reimplement Vanity Plates from Problem Set 2, restructuring your code 
per the below, wherein is_valid still expects a str as input and returns 
True if that str meets all requirements and False if it does not, but 
main is only called if the value of __name__ is "__main__".

Then, in a file called test_plates.py, implement four or more functions 
that collectively test your implementation of is_valid thoroughly, each 
of whose names should begin with test_ so that you can execute your tests.
"""

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    if not valid_first_two_chars(s):
        return False
    if not valid_plate_length(s):
        return False
    if not valid_plate_punct(s):
        return False
    if not valid_num_indexes(s):
        return False
    else:
        return True
 

def valid_first_two_chars(plate: str) -> bool:
    try:
        if plate[0].isnumeric() or plate[1].isnumeric():
            return False
        return True
    except IndexError:
        return False


def valid_plate_length(plate: str) -> bool:
    if len(plate) < 2 or len(plate) > 6:
        return False
    return True


def valid_plate_punct(plate: str) -> bool:
    for c in plate:
        if not c.isalnum():
            return False
    return True


def valid_num_indexes(plate: str) -> bool:
    first_num = ""
    plate_slice = plate[2:]
    for c in plate_slice:
        if c.isnumeric():
            if first_num == "":
                first_num = c
            if first_num == "0":
                return False
        else:
            if first_num != "":
                return False
    return True



if __name__ == "__main__":
    main()