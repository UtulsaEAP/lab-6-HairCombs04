"""
Name: Bradyn Combs
Lab Time: 2/29/24 2:00 PM
"""

def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10
    total = 0
   
   #type your code here 
    print("ZyCar Wash")
    print("Base car wash -- $10")
    total = total + base_wash
    if service_choice1 in services:
        value = services[service_choice1]
        total = total + value
        print('{} - ${}'.format(service_choice1, value))
    if service_choice2 in services:
        value = services[service_choice2]
        total = total + value
        print('{} - ${}'.format(service_choice2, value))
    print('----')
    print("Total price: ${}".format(total))



    
if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input()
    service_choice2 = input()

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)
