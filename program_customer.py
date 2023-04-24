from colorama import Fore
from dateutil import parser
import json
import time
import data_mongo
import pandas
logged = False

def run():
    global logged

    while True:
        show_commands()
        action = input().strip().lower()
        if action == 'l' and not logged:
            log_into_account()
        elif action == 'c' and not logged:
            registration()
        elif action == 'v':
            if not logged:
                print(Fore.RED + 'First you need to log into your account')
                print()
            else: show_cars()
        elif action == '1':
            if not logged:
                print(Fore.RED + 'First you need to log into your account')
                print()
            else: sort_cars_by_brand()
        elif action == '2':
            if not logged:
                print(Fore.RED + 'First you need to log into your account')
                print()
            else: sort_cars_by_model()
        elif action == '3':
            if not logged:
                print(Fore.RED + 'First you need to log into your account')
                print()
            else: sort_cars_by_color()
        elif action == '4':
            if not logged:
                print(Fore.RED + 'First you need to log into your account')
                print()
            else: sort_by_year()
        elif action == '5':
            if not logged:
                print(Fore.RED + 'First you need to log into your account')
                print()
            else: sort_by_price()
        elif action == '6':
            if not logged:
                print(Fore.RED + 'First you need to log into your account')
                print()
            else: sort_by_mileage()
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
    print('[C]reate a account')
    print('[L]ogin to your account')
    print('[V]iew all cars in sale')
    print('[1]Sort by brand')
    print('[2]Sort by model')
    print('[3]Sort by color')
    print('[4]Sort by year')
    print('[5]Sort by price')
    print('[6]Sort by mileage')
    print('[M]ain menu')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()

def registration():
    print(' ****************** REGISTRATION **************** ')
    print()
    global logged
    file = open("customers.json", 'r+')
    data = json.load(file)
    name = str(input("What is your name? "))
    email = str(input("What is your email? "))
    password = str(input("Password:"))

    x = {
        "name": name,
        "email": email,
        "password": password
    }
    data.append(x)
    file.seek(0)
    json.dump(data, file, indent = 4)

    data_mongo.drop_from_customer()
    data_mongo.insert_from_customer()

    print(Fore.GREEN + 'Registration was successful')
    time.sleep(2)
    logged = True

def log_into_account():
    print(' ****************** LOGIN **************** ')
    print()
    global logged
    global email
    global password
    global name
    email = input('What is your email? ').strip().lower()
    password = input('Password: ')
    file = open("customers.json", 'r')
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

def show_cars():
    print(' ****************** Cars in Sale **************** ')
    print()
    with open('shop.json', 'r') as f:
        data = json.load(f)

    table = pandas.DataFrame(data)
    table.to_csv('cars.csv', index = False)
    print(table)
    time.sleep(2)

def sort_cars_by_brand():
    print(' ****************** Find Car By Brand **************** ')
    print()
    brand = str(input("Car brand name: "))
    file = open("shop.json", "r")
    data = json.load(file)
    for car in data:
        if car["brand"] == brand:
            print(f'{car["id"]}. {car["brand"]} {car["model"]} - year of manufacture: {car["year"]}, color: {car["color"]}, mileage: {car["mileage"]}, price: {car["price"]}')
            print()
    time.sleep(2)

def sort_cars_by_model():
    print(' ****************** Find Car By Model **************** ')
    print()
    model = input("Car model name: ")
    file = open("shop.json", "r")
    data = json.load(file)
    for car in data:
        if car["model"] == model:
            print(f'{car["id"]}. {car["brand"]} {car["model"]} - year of manufacture: {car["year"]}, color: {car["color"]}, mileage: {car["mileage"]}, price: {car["price"]}')
            print()
    time.sleep(2)

def sort_cars_by_color():
    print(' ****************** Find Car By Color **************** ')
    print()
    color = str(input("Cars color: "))
    file = open("shop.json", "r")
    data = json.load(file)
    for car in data:
        if car["color"] == color:
            print(f'{car["id"]}. {car["brand"]} {car["model"]} - year of manufacture: {car["year"]}, color: {car["color"]}, mileage: {car["mileage"]}, price: {car["price"]}')
            print()
    time.sleep(2)

def sort_by_year():
    print(' ****************** Sort Cars By Year **************** ')
    print()
    file = open('shop.json', 'r')
    data = json.load(file)
    action = input("[l]ess or [g]reater")
    if action == 'l':
        year = int(input("Higher bound of the year: "))
        for car in data:
            if car["year"] <= year:
                print(f'{car["id"]}. {car["brand"]} {car["model"]} - year of manufacture: {car["year"]}, color: {car["color"]}, mileage: {car["mileage"]}, price: {car["price"]}')
    elif action == 'g':
        year = int(input("Lower bound of the year: "))
        for car in data:
            if car["year"] >= year:
                print(f'{car["id"]}. {car["brand"]} {car["model"]} - year of manufacture: {car["year"]}, color: {car["color"]}, mileage: {car["mileage"]}, price: {car["price"]}')
    time.sleep(2)

def sort_by_price():
    print(' ****************** Sort Cars By Price **************** ')
    print()
    file = open('shop.json', 'r')
    data = json.load(file)
    action = input("[l]ess or [g]reater")
    if action == 'l':
        price = int(input("Maximum price value: "))
        for car in data:
            if car["price"] <= price:
                print(f'{car["id"]}. {car["brand"]} {car["model"]} - year of manufacture: {car["year"]}, color: {car["color"]}, mileage: {car["mileage"]}, price: {car["price"]}')
    elif action == 'g':
        price = int(input("Minimum price value: "))
        for car in data:
            if car["price"] >= price:
                print(f'{car["id"]}. {car["brand"]} {car["model"]} - year of manufacture: {car["year"]}, color: {car["color"]}, mileage: {car["mileage"]}, price: {car["price"]}')
    time.sleep(2)

def sort_by_mileage():
    print(' ****************** Sort Cars By Mileage **************** ')
    print()
    file = open('shop.json', 'r')
    data = json.load(file)
    action = input("[l]ess or [g]reater")
    if action == 'l':
        mileage = int(input("Higher bound of the year: "))
        for car in data:
            if car["mileage"] <= mileage:
                print(f'{car["id"]}. {car["brand"]} {car["model"]} - year of manufacture: {car["year"]}, color: {car["color"]}, mileage: {car["mileage"]}, price: {car["price"]}')
    elif action == 'g':
        mileage = int(input("Lower bound of the mileage: "))
        for car in data:
            if car["mileage"] >= mileage:
                print(f'{car["id"]}. {car["brand"]} {car["model"]} - year of manufacture: {car["year"]}, color: {car["color"]}, mileage: {car["mileage"]}, price: {car["price"]}')
    time.sleep(2)