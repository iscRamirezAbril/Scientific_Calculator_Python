import os

# This is the library that will help with text color.
from colorama import init, Fore
init(autoreset=True)

os.system("cls") # Clear the window
print(Fore.CYAN + "=============================================================================================")
print(Fore.CYAN + "                     --- Welcome to the Scientific Calculator! :D ---                        ")
print(Fore.CYAN + "=============================================================================================")

# Principal Menu
print("This is the principal menu.")
print("a. Basic Math Functions")
print("b. More Math Functions")
print("c. Trigonometric Functions")
print("d. Inverse Math Functions")
print("e. Exit")

Option = input("\nPlease, select an option: ")

# Secondary Menu
if Option == "a": 
    os.system("cls") # Clear the window
    print("a. Basic Math Functions")
    print("   1. Addition")
    print("   2. Subtraction")
    print("   3. Multiplication")
    print("   4. Division")
elif Option == "b"
    os.system("cls") # Clear the window
    print("b. More Math Functions")
    print("   1. Square of a number")
    print("   2. Cube of a number")
    print("   3. Number raised to the 10 power")
    print("   4. Percentage of a number")
    
