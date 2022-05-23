

def get_input():
    # Returns error from input as ValueError
    input = input("Enter a number: ")
    try:
        input = int(input)
    except ValueError:
        print("Invalid input")
        get_input()
    return input

def do_something(input):
    # Throws any error.
    try: 
        input = input * 2
    except Exception as e:
        print("An error occurred: ", e)
    return input

def main():
    # Throws any error. KeyboardInterrupt is specifically caught. 
    try:
        input = get_input()
        print(do_something(input))
    except Exception as e:
        if type(e) == KeyboardInterrupt:
            print("Keyboard interrupt")
        else:
            print("An error occurred: ", e)
            main()  