# <---------------------> #
# <----- Libraries -----> #
# <---------------------> #
import os
import sys
import msvcrt

# This is the library that will help with text color.
from colorama import init, Fore
init(autoreset = True)

contador = 1

# -------------------------- #
# ----- Principal Menu ----- #
# -------------------------- #
while(contador == 1):
    os.system("cls") # Clear the window
    print(Fore.CYAN + "=============================================================================================")
    print(Fore.CYAN + "                     --- Welcome to the Scientific Calculator! :D ---                        ")
    print(Fore.CYAN + "=============================================================================================")

    Option = int(input("This is the Principal Menu\n   1. Basic Math Functions\n   2. More Math Functions\n   3. Trigonometric Functions\n   4. Exit\n\nPlease, select an option: "))

    if(Option == 1):
        contador1 = 0
        os.system("cls") # Clear the window
        while(contador1 == 0):
            # -------------------------- #
            # ----- Secondary Menu ----- #
            # -------------------------- #
            Option = int(input("A. BASIC MATH FUNCTIONS\n   1. Addition\n   2. Substraction\n   3. Multiplication\n   4. Division\n   5. Square Root\n   6. Cube Root\n   7. Return\n\n Please, select an option: "))
            if Option == 1:
                print("Pending...")
            elif Option == 2:
                print("Pending...")
            elif Option == 3:
                print("Pending...")
            elif Option == 4:
                print("Pending...")
            elif Option == 5:
                print("Pending...")
            elif Option == 6:
                print("Pending...")
            elif Option == 7:
                print("Press any Key to return to the Main Menu...")
                msvcrt.getwch() # Press a key before returning to the main menu
                break
        os.system("cls") # Clear the window

    elif(Option == 2):
        contador1 = 0
        os.system("cls") # Clear the window
        while(contador1 == 0):
            # -------------------------- #
            # ----- Secondary Menu ----- #
            # -------------------------- #
            Option = int(input("B. MORE MATH FUNCTIONS\n   1. Square of a numbre\n   2. Cube of a number\n   3. Number Raised to x power\n   4. Number Raised to -1 power\n   5. Percentage of a number\n   6. Factorial\n   7. Logarithm\n   8. Natural Logarithm\n   9. Return\n\n Please, select an option: "))
            if Option == 1:
                print("Pending...")
            elif Option == 2:
                print("Pending...")
            elif Option == 3:
                print("Pending...")
            elif Option == 4:
                print("Pending...")
            elif Option == 5:
                print("Pending...")
            elif Option == 6:
                print("Pending...")
            elif Option == 7:
                print("Peding...")
            elif Option == 8:
                print("Pending...")
            elif Option == 9:
                print("Press any Key to return to the Main Menu...")
                msvcrt.getwch() # Press a key before returning to the main menu
                break
        os.system("cls") # Clear the window

    elif(Option == 3):
        contador2 == 0
        os.system("cls") # Clear the window
        while(contador2 == 0):
            # -------------------------- #
            # ----- Secondary Menu ----- #
            # -------------------------- #
        os.system("cls") # Clear the window
        print("Entraste al corte 3")
        contador = 1
    elif(Option == 4):
        sys.exit() # Close the window
    else:
        print("esa opcion no esta disponible")
        contador = 1