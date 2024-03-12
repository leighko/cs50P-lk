"""
implement a program that prompts the user for items, one 
per line, until the user inputs control-d (which is a 
common way of ending one’s input to a program). Then output 
the user’s grocery list in all uppercase, sorted alphabetically 
by item, prefixing each line with the number of times the user 
inputted that item. No need to pluralize the items. Treat the 
user’s input case-insensitively.
"""

def main():
    item_input = grocery_list()


def grocery_list():
    item_dict = {}
    while True:
        try:
            item = input().upper()
            if item not in item_dict:
                item_dict[item] = 1
            else:
                item_dict[item] = item_dict.get(item)+1
        except EOFError:
            for i in item_dict:
                print(f"{item_dict.get(i)} {i}")
            return
        except KeyError:
            pass


if __name__ == "__main__":
    main()