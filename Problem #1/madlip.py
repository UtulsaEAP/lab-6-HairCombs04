"""
Name: Bradyn Combs
Lab Time: 02/29/24 2:00 PM
"""

def food_input():
    user_input = input()
    tokens = user_input.split()
    #type you while  loop here
    while True:
        item = tokens[0]
        if item == 'quit':
            break
        count = tokens[1]
        print("Eating " + count + " " + item + " a day keeps you happy and healthy.")
    
if __name__ == "__main__":
    food_input()
