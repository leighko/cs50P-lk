import random

prompt = "Level: "

def main():
    user_level = get_level()
    output = generate_integer(user_level)
    print(f"Score: {output}")


def get_level() -> int:
    invalid_level = True
    while invalid_level:
        try:
            level = int(input(prompt))
            if level == 1:
                return 1
            elif level == 2:
                return 2
            elif level == 3:
                return 3
        except:
            pass


def generate_integer(level_return: int) -> int:
    user_incorrect = 0
    answers_correct = 0
    if level_return == 1:
        for i in range(10):
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            answer = x + y
            incorrect_answer = True
            while incorrect_answer:
                user_answer = int(input(f"{x} + {y} = " ))
                if user_answer != answer:
                    user_incorrect += 1
                    print("EEE")
                    if user_incorrect == 3:
                        print(f"{x} + {y} = {answer}")
                        incorrect_answer = False
                else:
                    answers_correct += 1
                    user_incorrect = 0
                    incorrect_answer = False
    elif level_return == 2:
        for i in range(10):
            x = random.randint(10, 20)
            y = random.randint(10, 20)
            answer = x + y
            incorrect_answer = True
            while incorrect_answer:
                user_answer = int(input(f"{x} + {y} = " ))
                if user_answer != answer:
                    user_incorrect += 1
                    print("EEE")
                    if user_incorrect == 3:
                        print(f"{x} + {y} = {answer}")
                        incorrect_answer = False
                else:
                    answers_correct += 1
                    user_incorrect = 0
                    incorrect_answer = False
    elif level_return == 3:
        for i in range(10):
            x = random.randint(20, 30)
            y = random.randint(20, 30)
            answer = x + y
            incorrect_answer = True
            while incorrect_answer:
                user_answer = int(input(f"{x} + {y} = " ))
                if user_answer != answer:
                    user_incorrect += 1
                    print("EEE")
                    if user_incorrect == 3:
                        print(f"{x} + {y} = {answer}")
                        user_incorrect = 0
                        incorrect_answer = False
                else:
                    answers_correct += 1
                    user_incorrect = 0
                    incorrect_answer = False
    return answers_correct
            

if __name__ == "__main__":
    main()