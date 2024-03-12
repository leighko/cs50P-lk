"""
implement a program that prompts the user for a date, anno Domini, 
in month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
wherein the month in the latter might be any of the values in the list 
below: [see MONTS]

Then output that same date in YYYY-MM-DD format. If the user’s input 
is not a valid date in either format, prompt the user again. Assume 
that every month has no more than 31 days; no need to validate whether 
a month has 28, 29, 30, or 31 days.
"""

MONTS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

prompt = "Date: "

class OutOfBoundsDateError(Exception):
    "String formatted as date had out of bounds month or day values"
    pass
    
    
def main():
    user_invalid_input = True
    while user_invalid_input:
        user_input = input(prompt)
        try:
            formatted_user_date = get_formatted_user_input(user_input)
            print(formatted_user_date)
            user_invalid_input = False
        except Exception as e:
            if type(e) is IndexError:
                print("Invalid month format.")
            elif type(e) is ValueError:
                print("Invalid day format.")
            elif type(e) is OutOfBoundsDateError:
                print("Date is out of range.")
            else:
                print(f"Unknown error caught: {e}")


def get_formatted_user_input(user_input: str) -> str:
    parsed_user_input = user_input.strip().replace(",", "").split()
    if parsed_user_input[0] in MONTS:
        return get_date_long(parsed_user_input)
    else:
        parsed_date_short = user_input.split("/")
        return get_date_short(parsed_date_short)
    
        
def get_date_long(date_list: list) -> str:
    """
        does thing from long
    """
    formatted_date = ""
    month = MONTS.index(date_list[0]) + 1
    formatted_date = f"{date_list[2]}-{month:02}-{int(date_list[1]):02}"
    return formatted_date


def get_date_short(date_list: list) -> str:
    formatted_date = ""
    if int(date_list[1]) <= 31 and int(date_list[0]) <= 12:
        formatted_date = f"{date_list[2]}-{int(date_list[0]):02}-{int(date_list[1]):02}"
        return formatted_date
    raise OutOfBoundsDateError()
    
    
        
# def updated_date(prompt):
#     while True:
#         try:
#             date_str = input(prompt)
#             date_long = date_str.replace(",", "").split(" ")
#             if date_long[0] in MONTS:
#                 month = MONTS.index(date_long[0]) + 1
#                 return print(f"{date_long[2]}-{month:02}-{int(date_long[1]):02}")
#                 # return a string ... do not return a print statement lol
#             else:
#                 date_short = date_str.split("/")
#                 if int(date_short[1]) <= 31 and int(date_short[0]) <= 12:
#                     return print(f"{date_short[2]}-{int(date_short[0]):02}-{int(date_short[1]):02}")
#         except (ValueError, IndexError):
#             pass


if __name__ == "__main__":
    main()