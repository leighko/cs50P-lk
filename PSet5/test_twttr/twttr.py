"""
reimplement Setting up my twttr from Problem Set 2, restructuring 
your code per the below, wherein shorten expects a str as input and 
returns that same str but with all vowels (A, E, I, O, and U) omitted, 
whether inputted in uppercase or lowercase.

Then, in a file called test_twttr.py, implement one or more functions 
that collectively test your implementation of shorten thoroughly, each 
of whose names should begin with test_ so that you can execute your tests.
"""

def main():
    word_input = input("Type a word: ")
    new_word = shorten(word_input)
    print(new_word)


def shorten(word: str) -> str:
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    for c in word:
        if c in vowels:
            word = word.replace(c, "")
    return word


if __name__ == "__main__":
    main()