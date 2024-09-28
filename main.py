import sqlite3
import string
import random

lower_char = string.ascii_lowercase
upper_char = string.ascii_uppercase
numbers = string.digits
special = string.punctuation


def generate_password():
    password = ""
    min_length = int(input("Enter a minimum length (above 4): "))
    lower_condition = input("Do you want lowercase letters (y or n)? ")
    upper_condition = input("Do you want uppercase letters (y or n)? ")
    numbers_condition = input("Do you want numbers (y or n)? ")
    special_condition = input("Do you want special characters (y or n)? ")

    while len(password) < min_length:

        if lower_condition == "y":
            password += lower_char[random.randint(0,len(lower_char)-1)]
        if upper_condition == "y":
            password += upper_char[random.randint(0,len(upper_char)-1)]
        if numbers_condition == "y":
            password += numbers[random.randint(0,len(numbers)-1)]
        if special_condition == "y":
            password += special[random.randint(0,len(special)-1)]
        
    return password
        

print(generate_password())






connection = sqlite3.connect("passwords.db")

cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS passwords 
               (id integer, password text, usage text)""")

connection.commit()
connection.close()