"""
Name: Bradyn Combs
Lab Time: 2/29/24 2:00 PM
"""

def check_palindrome(user_input):
 #type your code here
    start = 0
    end = len(user_input) - 1

    while (start < end):
        if (user_input[start] != user_input[end]):
            print(f'not a palindrome: {user_input}')
            return

        start += 1

        end -= 1

    print(f'palindrome: {user_input}')
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
