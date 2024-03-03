"""
Name: Bradyn Combs
Lab Time: 2/29/24 2:00 PM
"""

def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10
    total = 0
   
   #type your code here 
    description = ["ZyCar Wash", "Base car wash - $10"]
    if (service_choice1 != '-'):
        total += services[service_choice1]
        description.append(
            f'{service_choice1} - ${services[service_choice1]}'
        )
    if (service_choice2 != '-'):
        total += services[service_choice2]
        description.append(
            f'{service_choice2} - ${services[service_choice2]}'
        )
    total += base_wash
    for descriptionPart in description:
        print(descriptionPart)    
    print("-----")
    print(f'Total price: ${total}')

if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input()
    service_choice2 = input()

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)
