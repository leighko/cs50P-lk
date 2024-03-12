"""
implement a program that prompts the user for a fraction, 
formatted as X/Y, wherein each of X and Y is an integer, 
and then outputs, as a percentage rounded to the nearest 
integer, how much fuel is in the tank. If, though, 1% or 
less remains, output E instead to indicate that the tank 
is essentially empty. And if 99% or more remains, output 
F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, 
or Y is 0, instead prompt the user again. (It is not necessary 
for Y to be 4.) Be sure to catch any exceptions like ValueError 
or ZeroDivisionError.
"""

def main():
    fract = get_fraction("Fraction: ")
    print(fract)


def get_fraction(fraction):
    while True:
        try:
            n = input(fraction)
            n = n.replace("/", "")
            
            if n.isnumeric():
                if n[0] <= n[1]:
                    answer = round((int(n[0]) / int(n[1])) * 100)
                    break
        except (ValueError, ZeroDivisionError):
            pass
    
    if answer <= 1:
        return "E"
    elif answer >= 99 and answer <= 100:
        return "F"
    else:
        return f"{answer}%"
    

if __name__ == "__main__":
    main()