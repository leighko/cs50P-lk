"""
implement a program in Python that prompts the user for 
mass as an integer (in kilograms) and then outputs the 
equivalent number of Joules as an integer. Assume that 
the user will input an integer.
"""

# asks for input of mass as m
# calls emc() with m as an argument
# prints out "E: " with the correct calculation
def main():
    m = int(input("m: "))
    print(f"E: {emc(m)}")
    

# returns mc^2 
def emc(mass):
    calc = mass*(300000000)**2
    return calc


main()