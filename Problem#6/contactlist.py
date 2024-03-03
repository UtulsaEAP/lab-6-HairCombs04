"""
Name: Bradyn Combs
Lab Time: 2/29/24 2:00 PM
"""

def process_user_contacts(user_input):
    user_contacts = {}
    while True:
        try:
            name,phone = input().split()
        except:
            break
 
    user_contacts[name] = phone

    # Put word pairs into a dictionary
    
    # Get contact name from input, output contact's phone number
    user_input = input("Enter the contact name: ")
    if user_input in user_contacts:
        print(user_contacts[user_input])
    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
