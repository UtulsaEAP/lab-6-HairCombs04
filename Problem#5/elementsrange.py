"""
Name: Bradyn Combs
Lab Time: 2/29/24 2:00 PM
"""

def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
    for num in input_list:
        if (num >= min_val and num <= max_val):
            print(num, end=',')

if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = list(map(int, input().split()))

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val = map(int, input().split())

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(integer_list, min_val, max_val)
   
