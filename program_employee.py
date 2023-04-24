from colorama import Fore
from dateutil import parser
import json
import time
import data_mongo
import pandas

logged = False
email = None
password = None
name = None
id_counter = None

def run():
    global logged
    while True:
        show_commands()

        action = input().strip().lower()
        if action == 'l' and not logged:
            log_into_account()
        elif action == 'r':
            if not logged:
                print(Fore.RED + 'First you need to log into your account')
                print()
            else: registration()
        elif action == 'v':
            if not logged:
                print(Fore.RED + 'First you need to log into your account')
                print()
            else: show_cars()
        elif action == 'a':
            if not logged:
                print(Fore.RED + 'First you need to log into your account')
                print()
            else: add_car()
        elif action == 'u':
            if not logged:
                print(Fore.RED + 'First you need to log into your account')
                print()
            else: update_info_car()
        elif action == 'r':
            if not logged:
                print(Fore.RED + 'First you need to log into your account')
                print()
            else: remove_car()
        elif action == 'm':
            logged = False
            return
        elif action == 'x':
            data_mongo.drop_from_employee()
            data_mongo.insert_from_employee()
            data_mongo.drop_from_customer()
            data_mongo.insert_from_customer()
            data_mongo.drop_from_shop()
            data_mongo.insert_from_shop()
            exit()
        elif action == '?':
            run()
        else: 
            print(Fore.RED + 'Command is not found, Try again')
            run()
        
def show_commands():
    print(Fore.WHITE + 'What action would you like to take:')
    print('[L]ogin to your account')
    print('[R]egistration of new emloyee')
    print('[V]iew your cars')
    print('[A]dd new cars')
    print('[U]pdate information about a car')
    print('[R]emove car')
    print('[M]ain menu')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()

def log_into_account():
    print(' ****************** LOGIN **************** ')
    print()
    global logged
    global email
    global password
    global name
    email = input('What is your email? ').strip().lower()
    password = input('Password: ')
    file = open("employee.json", 'r')
    data = json.load(file)
    for i in data:
        if i["email"] == email and i["password"] == password:
            logged = True
            name = i["name"]
    
    if logged:
        print(Fore.GREEN + f'Logged in successfully. Welcome to our service {name}')
        print()

    else:
        print()
        print(Fore.RED + 'Something is going wrong')
        print('Try again!')
        log_into_account()
    
def registration():
    print(' ****************** REGISTRATION **************** ')
    print()
    file = open("employee.json", 'r+')
    data = json.load(file)
    name = str(input("What is his/her name? "))
    email = str(input("What is his/her email? "))
    password = str(input("Password:"))

    x = {
        "name": name,
        "email": email,
        "password": password
    }
    data.append(x)
    file.seek(0)
    json.dump(data, file, indent = 4)

    data_mongo.drop_from_employee()
    data_mongo.insert_from_employee()

    print(Fore.GREEN + 'Registration was successful')
    time.sleep(2)    

def show_cars():
    print(' ****************** Cars in Sale **************** ')
    print()
    with open('shop.json', 'r') as f:
        data = json.load(f)

    table = pandas.DataFrame(data)
    table.to_csv('cars.csv', index = False)
    print(table)
    time.sleep(2)

def add_car():
    print(' ****************** Add a New Car **************** ')
    print()
    file = open("shop.json", 'r+')
    data = json.load(file)
    brand = str(input("Brand: "))
    model = str(input("Model: "))
    year = int(input("Year of manufacture: "))
    color = str(input("Color: "))
    mileage = int(input("Mileage: "))
    price = int(input("Price: "))
    id_counter = 0
    for i in range(len(data) - 1, len(data) - 2, -1):
        id_counter = data[i]["id"] + 1

    x = {
        "id": id_counter,
        "brand": brand,
        "model": model,
        "year": year,
        "color": color,
        "mileage": mileage,
        "price": price
    }
    data.append(x)
    file.seek(0)
    json.dump(data, file, indent = 4)

    data_mongo.drop_from_shop()
    data_mongo.insert_from_shop()

    print(Fore.GREEN + 'The car was successfully added to the list')
    time.sleep(2)

def update_info_car():
    car_id = int(input("Enter the ID of the car you want to update: "))
    flag = False
    with open("shop.json", 'r') as file:
        data = json.load(file)

    for car in data:
        if car["id"] == car_id:
            print("Insert new information")
            print()
            car["brand"] = input("Brand: ")
            car["model"] = input("Model: ")
            car["year"] = int(input("Year of manufacture: "))
            car["color"] = input("Color: ")
            car["mileage"] = int(input("Mileage: "))
            car["price"] = int(input("Price: "))
            flag = True


    with open("shop.json", 'w') as file:
        json.dump(data, file, indent=4)
    if flag:
        print(Fore.GREEN + 'The information was successfully updated to the list')
    else: print(Fore.RED + 'ERROR. TRY AGAIN!')
    data_mongo.drop_from_shop()
    data_mongo.insert_from_shop()
    time.sleep(2)

def remove_car():
    car_id = int(input("Enter the ID of the car you want to remove: "))
    flag = False
    with open("shop.json", 'r') as file:
        data = json.load(file)
    
    for idx, car in enumerate(data):
        if car["id"] == car_id:
            data.pop(idx)
            flag = True
            print(Fore.GREEN + "The car is removed from list")

    if not flag:
        print(Fore.RED + 'ERROR. TRY AGAIN!')
    with open("shop.json", 'w') as file:
        json.dump(data, file, indent=4)
    data_mongo.drop_from_shop()
    data_mongo.insert_from_shop()
