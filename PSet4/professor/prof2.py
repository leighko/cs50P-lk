"""
implement a program that:

    Prompts the user for a level, n. If the user does not input 1, 2, or 3, 
        the program should prompt again.
    Randomly generates ten (10) math problems formatted as X + Y = , wherein
        each of X and Y is a non-negative integer with n digits. No need to 
        support operations other than addition (+).
    Prompts the user to solve each of those problems. If an answer is not 
        correct (or not even a number), the program should output EEE and 
        prompt the user again, allowing the user up to three tries in total 
        for that problem. If the user has still not answered correctly after
        three tries, the program should output the correct answer.
    The program should ultimately output the user’s score: the number of 
        correct answers out of 10.
    
    Structure your program as follows, wherein get_level prompts (and, 
    if need be, re-prompts) the user for a level and returns 1, 2, or 3, 
    and generate_integer returns a randomly generated non-negative integer 
    with level digits or raises a ValueError if level is not 1, 2, or 3:
"""

import random

prompt = "Level: "
LEVELS = [1, 2, 3]


def main():
    user_level = get_level()
    equation_and_solutions = generate_equations_and_solutions(user_level)
    
    score = 0
    for key in equation_and_solutions:
        user_wrong_answer = 0
        wrong_answer = True
        while wrong_answer:
            try:
                user_answer = int(input(f"{key} = "))
                if user_answer != equation_and_solutions.get(key):
                    print("EEE")
                    user_wrong_answer += 1
                    if user_wrong_answer >= 3:
                        print(f"{key} = {equation_and_solutions.get(key)}")
                        wrong_answer = False
                else:
                    score += 1
                    wrong_answer = False
            except ValueError:
                print("EEE")
                user_wrong_answer += 1
                if user_wrong_answer >= 3:
                    print(f"{key} = {equation_and_solutions.get(key)}")
                    wrong_answer = False
    print(f"Score: {score}")


def get_level() -> int:
    invalid_level = True
    while invalid_level:
        try:
            user_input = int(input(prompt))
            if user_input in LEVELS:
                return user_input
        except ValueError:
            pass


def generate_equations_and_solutions(level: int) -> dict:
    math_prob_dict = {}
    for i in range(10):
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        if level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        if level == 3:
            x = random.randint(100, 200)
            y = random.randint(100, 200)
        math_prob = f"{x} + {y}"
        answer = x + y
        math_prob_dict[math_prob] = answer
    return math_prob_dict


if __name__ == "__main__":
    main()