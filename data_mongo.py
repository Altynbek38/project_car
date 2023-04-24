from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['car_zone']

def insert_from_employee():
    with open('employee.json') as f:
        data_employee = json.load(f)
    collection_employee = db['employee']
    collection_employee.insert_many(data_employee)

def insert_from_customer():
    with open('customers.json') as f:
        data_customer = json.load(f)
    collection_customer = db['customers']
    collection_customer.insert_many(data_customer)

def insert_from_shop():
    with open('shop.json') as f:
        data_shop = json.load(f)
    collection_shop = db['shop']
    collection_shop.insert_many(data_shop)

def drop_from_employee():
    collection_employee = db['employee']
    query = {}
    collection_employee.delete_many(query)

def drop_from_customer():
    collection_customer = db['customers']
    query = {}
    collection_customer.delete_many(query)

def drop_from_shop():
    collection_shop = db['shop']
    query = {}
    collection_shop.delete_many(query)