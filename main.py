import json
from colorama import Fore
import program_customer
import program_employee
import mongoengine

def global_init():
    mongoengine.register_connection(alias='core', name='car_zone')

def main():
    print_header()
    global_init()

    try:
        while True:
            if find_user_intent() == 'customer':
                program_customer.run()
            else:
                program_employee.run()
    except KeyboardInterrupt:
        return

def print_header():
    car_zone = """
    
    ######################      ####################        ####################                
    ######################      ####################        ####################
    ######                      ####            ####        ####            ####
    ######                      ####            ####        ####            ####
    ######                      ####            ####        ####            ####
    ######                      ####################        ####################
    ######                      ####################        ####################
    ######                      ####            ####        ####      #####
    ######                      ####            ####        ####       #####  
    ######                      ####            ####        ####         #####
    ######################      ####            ####        ####          #####   
    ######################      ####            ####        ####           ##### 

    """

    print(Fore.WHITE + '****************  Car Zone  ****************')
    print(Fore.GREEN + car_zone)
    print(Fore.WHITE + '*********************************************')
    print()
    print("Welcome to Best Car Dealership!")
    print("Who are you?")
    print()

def find_user_intent():
    print("[c] A customer of a used car dealership")
    print("[e] Used car dealership employee ")
    print()
    choice = input("Are you a [c]ustomer or [e]mployee? ")
    if choice == 'e':
        return 'employee'
    elif choice == 'c':
        return 'customer'
    else:
        print('Error, try again')
        print()
        find_user_intent()

def file_read():
    with open('shop.json', 'r') as file:
        data = json.load(file)
    return data

def file_write(data):
    with open('shop.json', 'w') as file:
        json.dump(data, file)

def file_append(data):
    with open('shop.json', 'a') as file:
        file.write(data)

if __name__ == '__main__':
    main()