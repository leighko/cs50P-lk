"""
implement a program that prompts the user for the 
name of a variable in camel case and outputs the 
corresponding name in snake case. Assume that the 
user’s input will indeed be in camel case.
"""

def main():
    camel = input("camelCase: ")
    camel_to_snake(camel)


def camel_to_snake(camel_case):
    snake = ""
    for c in camel_case:
        if c.isupper():
            snake += "_" + c.lower()
        else:
            snake += c
    print(f"snake_case: {snake}")

            
if __name__ == "__main__":
    main()