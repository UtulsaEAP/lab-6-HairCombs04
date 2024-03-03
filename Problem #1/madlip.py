"""
Name: Bradyn Combs
Lab Time: 2/29/24 2:00 PM
"""

def food_input():
    user_input = input()
    tokens = user_input.split()
    #type you while  loop here
    while (True):
        itemToken = tokens[0]
        numberToken = tokens[1]
        if (itemToken == "quit" and numberToken == "0"):
            break
        print(f'Eating {numberToken} {itemToken} a day keeps you happy and healthy.')
        
        user_input = input()
        tokens = user_input.split()
if __name__ == "__main__":
    food_input()
