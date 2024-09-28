import string
import random

# All characters to be used for password generation
lower_char = string.ascii_lowercase
upper_char = string.ascii_uppercase
numbers = string.digits
special = string.punctuation

def generate_password():
    password = ""


    # Conditions for the password
    min_length = int(input("Enter a minimum length (above 4): "))
    while min_length <= 4:
        print("That number is not above 4.")
        min_length = int(input("Enter a minimum length (above 4): "))

    lower_condition = input("Do you want lowercase letters (y or n)? ").lower()
    while lower_condition != "y" and lower_condition != "n":
        print("Please choose y or n.")
        lower_condition = input("Do you want lowercase letters (y or n)? ").lower()

    upper_condition = input("Do you want uppercase letters (y or n)? ").lower()
    while upper_condition != "y" and upper_condition != "n":
        print("Please choose y or n.")
        upper_condition = input("Do you want uppercase letters (y or n)? ").lower()

    numbers_condition = input("Do you want numbers (y or n)? ").lower()
    while numbers_condition != "y" and numbers_condition != "n":
        print("Please choose y or n.")
        numbers_condition = input("Do you want numbers (y or n)? ").lower()

    special_condition = input("Do you want special characters (y or n)? ").lower()
    while special_condition != "y" and special_condition != "n":
        print("Please choose y or n.")
        special_condition = input("Do you want special characters (y or n)? ").lower()


    while len(password) < min_length:

        # Adds characters based on previous conditions
        if lower_condition == "y":
            password += lower_char[random.randint(0,len(lower_char)-1)]
        if upper_condition == "y":
            password += upper_char[random.randint(0,len(upper_char)-1)]
        if numbers_condition == "y":
            password += numbers[random.randint(0,len(numbers)-1)]
        if special_condition == "y":
            password += special[random.randint(0,len(special)-1)]
        
    return password

print("Welcome to Password Generator")
run = True
while run:
    print()
    generated_password = generate_password()
    print("Your generated password is: " + generated_password)
    
    loop = input("Would you like to continue (y or n)? ")
    if loop == "n":
        run = False
