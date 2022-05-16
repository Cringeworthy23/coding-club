"""
This script is a python calculator that can be used to perform basic math operations. 
More advanced math must either be handwritten or imported from a library.

This basic calculator I have compressed as much as I can while retaining error handling.
"""
import os

def get_choice():
    try: 
        choice = int(input("""
Please choose an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponent
        """))
    except Exception:
        print("That is not a function. Please try again.")
        os.system("clear||cls")
        choice = get_choice()
    if choice not in range(1, 6):
        print("That is not a function. Please try again.")
        os.system("clear||cls")
        choice = get_choice()
    return choice

def get_numbers():
    try:
        num1 = int(input("Please enter the first number: "))
        num2 = int(input("Please enter the second number: "))
    except Exception:
        print("That is not a number. Please try again.")
        num1, num2 = get_numbers()
    return num1, num2

def main():
    print("Welcome to my calculator, coded in Python!")
    choice = get_choice()
    num1, num2 = get_numbers()
    if choice == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == 2:
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == 3:
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == 4:
        print(f"{num1} / {num2} = {num1 / num2}")
    elif choice == 5:
        print(f"{num1} ** {num2} = {num1 ** num2}")
    repeat = input("Would you like to perform another operation? Default is no. (y/n): ")
    if repeat == "y":
        os.system("clear||cls")
        main()

main()