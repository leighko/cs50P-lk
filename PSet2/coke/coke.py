"""
implement a program that prompts the user to insert 
a coin, one at a time, each time informing the user 
of the amount due. Once the user has inputted at least 
50 cents, output how many cents in change the user is 
owed. Assume that the user will only input integers, 
and ignore any integer that isn’t an accepted denomination.
"""

due = 50

while due > 0:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    
    if coin in [25, 10, 5]:
        due -= coin

change = abs(due)
print(f"Change Owed: {change}")