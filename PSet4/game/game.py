"""
implement a program that:

    Prompts the user for a level, n. If the user does not input a positive 
        integer, the program should prompt again.
    Randomly generates an integer between 1 and n, inclusive, using the 
        random module.
    Prompts the user to guess that integer. If the guess is not a positive 
        integer, the program should prompt the user again.
        If the guess is smaller than that integer, the program should output
            Too small! and prompt the user again.
        If the guess is larger than that integer, the program should output 
            Too large! and prompt the user again.
        If the guess is the same as that integer, the program should output 
            Just right! and exit.
"""

import random

prompt = "Level: "


def main():
    invalid_input = True
    while invalid_input:
        try:
            n = int(input(prompt))
            if n > 0:
                comp_num = generate_rand_num(level=n)
                invalid_input = False
        except:
            pass
    compare_input_and_randnum(rand_num=comp_num)


def generate_rand_num(level: int) -> int:
    random_num = random.randint(1,level)
    return random_num
    
        
def compare_input_and_randnum(rand_num: int) -> None:
    guess_not_correct = True
    while guess_not_correct:
        try:
            guess = int(input("Guess: "))
            if guess > rand_num:
                print("Too large!")
            elif guess < rand_num and guess > 0:
                print("Too small!")
            elif guess == rand_num:
                print("Just right!")
                guess_not_correct = False 
        except:
            pass


if __name__ == "__main__":
    main()