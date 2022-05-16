"""
This script is a python calculator that can be used to perform basic math operations. 
More advanced math must either be handwritten or imported from a library.

This basic calculator uses functions to compress the code.
"""
import os
def add(num1, num2):
    answer = num1 + num2
    return answer

def subtract(num1, num2):
    answer = num1 - num2
    return answer

def multiply(num1, num2):
    answer = num1 * num2
    return answer

def divide(num1, num2):
    answer = num1 / num2
    return answer

def exponent(num1, num2):
    answer = num1 ** num2
    return answer

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
    except Exception as e:
        print(e)
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
    except Exception as e:
        print(e)
        print("That is not a number. Please try again.")
        num1, num2 = get_numbers()
    return num1, num2

def main():
    print("Welcome to my calculator, coded in Python!")
    choice = get_choice()
    num1, num2 = get_numbers()
    if choice == 1:
        answer = add(num1, num2)
        print(f"{num1} + {num2} = {answer}")
    elif choice == 2:
        answer = subtract(num1, num2)
        print(f"{num1} - {num2} = {answer}")
    elif choice == 3:
        answer = multiply(num1, num2)
        print(f"{num1} * {num2} = {answer}")
    elif choice == 4:
        answer = divide(num1, num2)
        print(f"{num1} / {num2} = {answer}")
    elif choice == 5:
        answer = exponent(num1, num2)
        print(f"{num1} ** {num2} = {answer}")
    repeat = input("Would you like to perform another operation? Default is no. (y/n): ")
    if repeat == "y":
        os.system("clear||cls")
        main()


main()
