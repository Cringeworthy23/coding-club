"""
This script is a python calculator that can be used to perform basic math operations. 
More advanced math must either be handwritten or imported from a library.
"""
running = True
while running == True:
    print("Welcome to my calculator, coded in Python!")
    choice = int(input("""
    Please choose an operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exponent
    """))

    if choice == 1: 
        print("You have chosen addition.")
        try:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
        except Exception as e: 
            print(e)
            print("That is not a number. Please try again.")
        answer = num1 + num2
        print(answer)

    elif choice == 2:
        print("You have chosen subtraction.")
        try:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
        except Exception as e:
            print(e)
            print("That is not a number. Please try again.")
        answer = num1 - num2
        print(answer)
    elif choice == 3:
        print("You have chosen multiplication.")
        try:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
        except Exception as e:
            print(e)
            print("That is not a number. Please try again.")
        answer = num1 * num2
        print(answer)
    elif choice == 4:
        print("You have chosen division.")
        try:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
        except Exception as e:
            print(e)
            print("That is not a number. Please try again.")
        answer = num1 / num2
        print(answer)
    elif choice == 5:
        print("You have chosen exponent.")
        try:
            num1 = int(input("Please enter the first number: "))
            num2 = int(input("Please enter the second number: "))
        except Exception as e:
            print(e)
            print("That is not a number. Please try again.")
        answer = num1 ** num2
        print(answer)
    else:
        print("That is not a valid choice. Please try again.")
    repeat = input("Would you like to perform another operation? (y/n): ")
    if repeat == "y":
        running = True
    else: 
        running = False
print("Goodbye!")