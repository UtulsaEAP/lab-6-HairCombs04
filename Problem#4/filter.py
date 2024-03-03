"""
Name: Bradyn Combs
Lab Time: 2/29/24 2:00 PM
"""

def process_and_print(input_string):
    # Split into separate strings
    numbers = input_string.split()
    # Convert strings to integers and filter out negative values
    numbers = numbers = [int(x) for x in numbers if int(x) >= 0]
    numbers = list(map(int, input().split()))
    # Sort integers in reverse order
    negative_numbers = sorted(filter(lambda x: x < 0, numbers), reverse=True)
    # Print sorted integers
    for num in negative_numbers:
      print(num, end=' ')

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
