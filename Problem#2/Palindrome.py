"""
Name: Bradyn Combs
Lab Time: 2/29/24 2:00 PM
"""

def check_palindrome(user_input):
 #type your code here
    user_input = input()
    normal = ""
    reverse = ""
    for i in range(len(user_input)):
        if user_input[i].isalpha():
            normal += user_input[i].lower()
            reverse = user_input[i].lower() + reverse
        if normal == reverse:
            print("palindrom: " + user_input)
        else:
            print("not a palindrome " + user_input)
if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
