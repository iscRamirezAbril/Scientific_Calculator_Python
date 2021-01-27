# <---------------------> #
# <----- Libraries -----> #
# <---------------------> #
import os
import sys

# This is the library that will help with text color.
from colorama import init, Fore
init(autoreset=True)

os.system("cls") # Clear the window
print(Fore.CYAN + "=============================================================================================")
print(Fore.CYAN + "                     --- Welcome to the Scientific Calculator! :D ---                        ")
print(Fore.CYAN + "=============================================================================================")

# -------------------------- #
# ----- Principal Menu ----- #
# -------------------------- #
print("This is the principal menu.")
print("a. Basic Math Functions")
print("b. More Math Functions")
print("c. Trigonometric Functions")
print("d. Exit")

Option = input("\nPlease, select an option: ")

# -------------------------- #
# ----- Secondary Menu ----- #
# -------------------------- #
    # If the opiton selected is "a"
if Option == "a": 
    os.system("cls") # Clear the window
    print("a. Basic Math Functions")
    print("   1. Addition")
    print("   2. Subtraction")
    print("   3. Multiplication")
    print("   4. Division")
    print("   5. Square Root")
    print("   6. Cube Root")
    # If the opiton selected is "b"
elif Option == "b":
    os.system("cls") # Clear the window
    print("b. Extra Math Functions")
    print("   1. Square of a number")
    print("   2. Cube of a number")
    print("   3. Number raised to x power")
    print("   4. Number raised to -1 power")
    print("   5. Percentage of a number")
    print("   6. Factorial")
    print("   7. Logarithm")
    print("   8. Natural logarithm")
    # If the opiton selected is "c"
elif Option == "c":
    os.system("cls") # Clear the window
    print("c. Trigonometric Functions")
    print("   A) Basic Trigonometric Functions")
    print("   B) Inverse Trigonometric Functions")
    print("   C) Hiperbolic Trigonometric Functions")
    
    Option = input("\nWich option do you chose? ")

    # -------------------------------------------- #
    # --- Menu for the Trigonometric Functions --- #
    # -------------------------------------------- #
        # If the opiton selected is "A"
    if Option == "A":
        os.system("cls") # Clear the window
        print("A) Basic Trigonometric Functions")
        print("   1. Sine [sin(x)]")
        print("   2. Cosine [cos(x)]")
        print("   3. Tangemt [tan(x)]")
        print("   4. Secant [sec(x)]")
        print("   5. Cosecant [csc(x)]")
        print("   6. Cotangent [cot(x)]")
        # If the opiton selected is "B"
    elif Option == "B":
        os.system("cls") # Clear the window
        print("B) Inverse Trigonometric Functions")
        print("   1. Arcsin(x)")
        print("   2. Arccos(x)")
        print("   3. Arctan(x)")
        # If the opiton selected is "C"
    elif Option == "C":
        os.system("cls") # Clear the window
        print("C) Hiperbolic Trigonometric Functions")
        print("   1. sinh(x)")
        print("   2. cosh(x)")
        print("   3. tanh(x)")
    # If the opiton selected is "d"
elif Option == "d":
    Option = input("Are you sure you want to leave? [Yes / No]: ")
    if Option == "Yes":
        sys.exit("Thanks for using this program! Come back soon! :D") # Close the program