import classes_functions as cf
import time
from colorama import Fore, Back, Style, init


print("\033[0;32;40mAt the beginning of the file, we import our other file, classes_functions. ")
time.sleep(2)
print("\033[2;31;40m import classes_functions as cf")
time.sleep(1)
print('\033[0;0mwe import as cf in order to save us time typing out the whole "classes_functions" instead of just typing "cf" ')
time.sleep(1)

print(
"""You can import raw functions, like this: 
\033[2;31;40mfrom classes_functions import *
\033[0;0m
Now, it is as if the functions are defined within this file, yet they are saved somewhere else. 
This is useful if you want to import a function from another file, but you don't want to have to write the whole function.
This is also how pip and imported modules work. """
)
time.sleep(3)
print(
    """The following function was imported from another file: 
    \033[2;32;40mcf.function()\033[2;35;40m"""
)

cf.function()

time.sleep(3)
print(
    """\033[0;0m
The following class was imported from another file: 
\033[2;32;40m
goofball = cf.goofball()
\033[0;0m
When we import classes, we either import the class from the file, using this documentation: 
\033[2;32;40m
from classes_functions import goofball
\033[0;0m
OR
we define the class as a variable in this file, like this:
\033[2;32;40m
goofball = cf.goofball()
\033[0;0m
Now, we can use the class like this:
\033[2;32;40m
goofball.print_self("I'm a goofball")
\033[2;35;40m
"""
)
goofball = cf.goofball()
goofball.print_self("I'm a goofball")

time.sleep(5)
# We took this variable from Project 3\classes_functions.py:
print("""\033[1;37;40mNow, we can also borrow variables from other files as well: 
\033[2;32;40m
var2 = cf.var2
print(var2)
\033[2;35;40m"""
)
print(cf.var2)
print("\033[0;32;40mThank you for reading this file.\033[0;0m")

temp = input()
print("\033[2;37;40mAh, so you found the hidden stuff.")
time.sleep(1)
print("\033[2;37;40mI'm sure you're wondering how I managed to color my text! \033[0;0m")
time.sleep(1)
print("\033[1;31;44mThere's this neat feature in python called ANSI escape codes.")
print("\033[4;36;47mThe full docs can be found somewhere on the internet.\033[0;0m")
print("\033[2;37;40mI used the escape sequence \033[2;35;40m\033[0;0m\033[2;37;40m to turn off all colors. \033[0;0m")
time.sleep(1)



init(autoreset=True)
print(Fore.GREEN + "ANSI Codes can be confusing. They are also not universal: Some programs and terminals prefer RGB codes, etc. \nTry using the" + Fore.RED + "colorama" + Fore.GREEN + " module.")
time.sleep(3)
print("These are the basic commands:")

print(
    Fore.RED + "Fore.RED\n" + 
Fore.GREEN + "Fore.GREEN\n" + 
Fore.YELLOW + "Fore.YELLOW\n" + 
Fore.BLUE + "Fore.BLUE\n" + 
Fore.MAGENTA + "Fore.MAGENTA\n" + 
Fore.CYAN + "Fore.CYAN\n" + 
Fore.WHITE + "Fore.WHITE\n"
)

time.sleep(3)
print("Instead of including the escape sequence, or even the colorama exit code, you can pass a parameter into the init() command:" + 
Fore.BLUE + "init(autoreset=True)" + Fore.GREEN + " \nThis will reset the colorama settings after every print() function.")
time.sleep(3)
print("Read the source code of this file to see how I used colorama to color my text.")
time.sleep(1)
print("Check it out:" + Fore.CYAN + Back.WHITE + "https://github.com/Cringeworthy23/coding-club/tree/main/Project%203/main.py")
time.sleep(0.5)
print(Fore.YELLOW + "I have been uploading scripts as required to GitHub. \nI will be updating this repository as we progress. \nMost, if not all of coding club should end up there. \nYou will see my ideas for what to do, and see what we ended up actually doing. ")