"""
implement a program that prompts the user for a str 
of text and then outputs that same text but with all 
vowels (A, E, I, O, and U) omitted, whether inputted 
in uppercase or lowercase.
"""

def main():
    user_s = input("Input: ")
    vowel_remove(user_s)


def vowel_remove(s):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        
    for c in s: 
        if c in vowels:
            # .replace() returns a copy of modified string, not s itself. have to reassign
            s = s.replace(c, "")
    
    print(s)


if __name__ == "__main__":
    main()