"""
reimplement Fuel Gauge from Problem Set 3, restructuring your code per 
the below, wherein:

    convert expects a str in X/Y format as input, wherein each of X and 
        Y is an integer, and returns that fraction as a percentage rounded 
        to the nearest int between 0 and 100, inclusive. If X and/or Y is 
        not an integer, or if X is greater than Y, then convert should raise
        a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
    gauge expects an int and returns a str that is:
        "E" if that int is less than or equal to 1,
        "F" if that int is greater than or equal to 99,
        and "Z%" otherwise, wherein Z is that same int.

Then, in a file called test_fuel.py, implement two or more functions that 
collectively test your implementations of convert and gauge thoroughly, 
each of whose names should begin with test_ so that you can execute your tests.
"""

prompt = "Fraction: "

     
def main():
    invalid_input = True
    while invalid_input:
        try:
            user_input = input(prompt).strip()
            conversion = convert(user_input)
            invalid_input = False
        except:
            pass
    final = gauge(conversion)
    print(final)

    
def convert(fraction: str) -> int:
    try:
        f_tuple = fraction.partition("/")
        x, y = int(f_tuple[0]), int(f_tuple[2])
        percent = round((int(f_tuple[0]) / int(f_tuple[2])) * 100)
    except (ValueError, ZeroDivisionError):
        pass
    return percent
    

def gauge(percentage: int) -> str:
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()