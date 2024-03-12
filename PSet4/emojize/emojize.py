"""
implement a program that prompts the user for a str in 
English and then outputs the “emojized” version of that 
str, converting any codes (or aliases) therein to their 
corresponding emoji.
"""

import emoji

prompt = "Input: "
    

def main():
    user_input = input(prompt)
    emoji_output = emoji_converter(user_input)
    print(f"Ouput: {emoji_output}")
    

def emoji_converter(user_str: str) -> str:
    user_list = user_str.split()
    for item in user_list:
        if item.startswith(":"):
            emo = emoji.emojize(item)
            user_list.remove(item)
            user_list.append(emo)
    new_user_str = " ".join(user_list)
    return new_user_str
        


# output = emoji_conversion(user_input)
# parser_output = input_parser(user_input)
# emoji_output = emoji_conversion(parser_output)

# def input_parser(user_str: str) -> list:
#     user_list = user_str.split()
#     return user_list


# def emoji_conversion(emoji_str: str) -> str:
#     invalid_emoji_input = True
#     while invalid_emoji_input:
#         try:
#             emo = emoji.emojize(emoji_str)
#             invalid_emoji_input = False
#             return emo
#         except:
#             pass


if __name__ == "__main__":
    main()