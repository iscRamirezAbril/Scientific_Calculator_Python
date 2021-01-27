import os

# This is the library that will help with text color.
from colorama import init, Fore
init(autoreset=True)

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
    os.system("cls") # Clear
    print("a. Basic Math Functions")
    print("   1. Addition")
    print("   2. Sustraction")
    print("   3. Multiplication")
    print("   4. Division")
elif Option == "b"
