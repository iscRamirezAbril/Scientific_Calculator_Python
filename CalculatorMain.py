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
    # If the opiton selected is "a"
if Option == "a": 
    os.system("cls") # Clear the window
    print("a. Basic Math Functions")
    print("   1. Addition")
    print("   2. Subtraction")
    print("   3. Multiplication")
    print("   4. Division")
    # If the opiton selected is "b"
elif Option == "b":
    os.system("cls") # Clear the window
    print("b. Extra Math Functions")
    print("   1. Square of a number")
    print("   2. Cube of a number")
    print("   3. Number raised to the 10 power")
    print("   4. Negative raised of a number")
    print("   5. Percentage of a number")
    print("   6. Factorial")
    print("   7. Logarithm of a number")
    print("   8. Natural logarithm of a number")
    # If the opiton selected is "c"
elif Option == "c":
    os.system("cls") # Clear the window
    print("c. Trigonometric Functions")