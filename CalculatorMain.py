# <---------------------> #
# <----- Libraries -----> #
# <---------------------> #
import os
import sys
import msvcrt
from FunctionLibrary import * # My library
from colorama import init, Fore # This is the library that will help with text color.
init(autoreset = True)

index = 1

# -------------------------- #
# ----- Principal Menu ----- #
# -------------------------- #
while(index == 1):
    os.system("cls") # Clear the window
    print(Fore.CYAN + "=============================================================================================")
    print(Fore.CYAN + "                     --- Welcome to the Scientific Calculator! :D ---                        ")
    print(Fore.CYAN + "=============================================================================================")

    Option = int(input("This is the Principal Menu\n   1. Basic Math Functions\n   2. More Math Functions\n   3. Trigonometric Functions\n   4. Exit\n\nPlease, select an option: "))

    if(Option == 1):
        index1 = 0
        os.system("cls") # Clear the window
        while(index1 == 0):
            # ------------------------------------- #
            # ----- Basic Math Functions Menu ----- #
            # ------------------------------------- #
            Option = int(input("A. BASIC MATH FUNCTIONS\n   1. Addition\n   2. Substraction\n   3. Multiplication\n   4. Division\n   5. Square Root\n   6. Cube Root\n   7. Return\n\nPlease, select an option: "))
            
            # Option for "Addition" function
            if Option == 1:
                Num1 = int(input("- Insert the first number: "))
                Num2 = int(input("- Insert the second number: "))
                objAdd = Addition(Num1, Num2) # Creation of an object from the class "Addition"
                AddResult = objAdd.AddOp(Num1, Num2) # Method call
                print("\nTHE ANSWER OF THE ADDITION IS: " + str(AddResult)) # Result

                print("\nPress any Key to return to the Basic Math Functions...")
                msvcrt.getwch() # Press a key before returning to the main menu
                os.system("cls") # Clear the window

            # Option for "Substraction" function
            elif Option == 2:
                Num1 = int(input("- Insert the first number: "))
                Num2 = int(input("- Insert the second number: "))
                objSubs = Substraction(Num1, Num2) # Creation of an object from the class "Addition"
                SubsResult = objSubs.SubsOp(Num1, Num2) # Method call
                print("\nTHE ANSWER OF THE SUBSTRACTION IS: " + str(SubsResult)) # Result

                print("\nPress any Key to return to the Basic Math Functions...")
                msvcrt.getwch() # Press a key before returning to the main menu
                os.system("cls") # Clear the window

            # Option for "Multiplication" function
            elif Option == 3:
                Num1 = int(input("- Insert the first number: "))
                Num2 = int(input("- Insert the second number: "))
                objMult = Multiplication(Num1, Num2) # Creation of an object from the class "Addition"
                MultResult = objMult.MultOp(Num1, Num2) # Method call
                print("\nTHE ANSWER OF THE MULTIPLICATION IS: " + str(MultResult)) # Result

                print("\nPress any Key to return to the Basic Math Functions...")
                msvcrt.getwch() # Press a key before returning to the main menu
                os.system("cls") # Clear the window

            # Option for "Division" function
            elif Option == 4:
                Num1 = int(input("- Insert the first number: "))
                Num2 = int(input("- Insert the second number: "))

                if Num2 == 0:
                    print("\nMATH ERROR!...")
                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the main menu
                    os.system("cls") # Clear the window
                else:
                    objDiv = Division(Num1, Num2) # Creation of an object from the class "Addition"
                    DivResult = objDiv.DivOp(Num1, Num2) # Method call
                    print("\nTHE ANSWER OF THE DIVIISON IS: " + str(DivResult)) # Result

                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the main menu
                    os.system("cls") # Clear the window

            # Option for "Square Root" function
            elif Option == 5:
                Num1 = int(input("- Insert the number that you want to calculate it square root: "))

                if Num1 < 0:
                    print("\nMATH ERROR!...")
                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the main menu
                    os.system("cls") # Clear the window
                else:
                    objSqrRoot = Square_Root(Num1) # Creation of an object from the class "Addition"
                    SqrRootResult = objSqrRoot.SquRootOp(Num1) # Method call
                    print("\nTHE ANSWER OF THE SQUARE ROOT IS: " + str(SqrRootResult)) # Result

                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the main menu
                    os.system("cls") # Clear the window

            # Option for "Cube Root" function
            elif Option == 6:
                Num1 = int(input("- Insert the number that you want to calculate it cube root: "))

                objCubeRoot = Cube_Root(Num1) # Creation of an object from the class "Addition"
                CubeRootResult = objCubeRoot.CubeRootOp(Num1) # Method call
                print("\nTHE ANSWER OF THE SQUARE ROOT IS: " + str(CubeRootResult)) # Result

                print("\nPress any Key to return to the Basic Math Functions...")
                msvcrt.getwch() # Press a key before returning to the main menu
                os.system("cls") # Clear the window

            elif Option == 7:
                print("Press any Key to return to the Main Menu...")
                msvcrt.getwch() # Press a key before returning to the main menu
                break
        os.system("cls") # Clear the window

    elif(Option == 2):
        index1 = 0
        os.system("cls") # Clear the window
        while(index1 == 0):
            # ------------------------------------ #
            # ----- More Math Functions Menu ----- #
            # ------------------------------------ #
            Option = int(input("B. MORE MATH FUNCTIONS\n   1. Square of a numbre\n   2. Cube of a number\n   3. Number Raised to x power\n   4. Number Raised to -1 power\n   5. Percentage of a number\n   6. Factorial\n   7. Logarithm\n   8. Natural Logarithm\n   9. Return\n\nPlease, select an option: "))
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
        index1 == 0
        os.system("cls") # Clear the window
        while(index1 == 0):
            # ---------------------------------------- #
            # ----- Trigonometric Functions Menu ----- #
            # ---------------------------------------- #
            Option = int(input("C. TRIGONOMETRIC FUNCTIONS\n   1. Basic Trigonometric Functions\n   2. Inverse Trigonometric Functions\n   3. Hiperbolic Trigonometric Functions\n   4. Return\n\nPlease, select an option: "))
            if Option == 1:
                index2 = 0
                os.system("cls") # Clear the window
                while(index2 == 0):
                    # ---------------------------------------------- #
                    # ----- Basic Trigonometric Functions Menu ----- #
                    # ---------------------------------------------- #
                    Option = int(input("I. BASIC TRIGONOMETRIC FUNCTIONS\n   1. Sine [sin(x)]\n   2. Cosine [cos(x)]\n   3. Tangent [tan(x)]\n   4. Secant [sec(x)]\n   5. Cosecant [csc(x)]\n   6. Cotangent [cot[x]]\n   7. Return\n\nPlease, select an option: "))
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
                        print("Press any Key to return to the Trigonometric Functions Menu...")
                        msvcrt.getwch() # Press a key before returning to the main menu
                        break
                os.system("cls") # Clear the window
            elif Option == 2:
                index2 = 0
                os.system("cls") # Clear the window
                while(index2 == 0):
                    # ------------------------------------------------ #
                    # ----- Inverse Trigonometric Functions Menu ----- #
                    # ------------------------------------------------ #
                    Option = int(input("II. INVERSE TRIGONOMETRIC FUNCTIONS\n   1. Arcsin(x)\n   2. Arccos(x)\n   3. Arctan(x)\n   4. Return\n\nPlease, select an option: "))
                    if Option == 1:
                        print("Pending...")
                    elif Option == 2:
                        print("Pending...")
                    elif Option == 3:
                        print("Pending...")
                    elif Option == 4:
                        print("Press any Key to return to the Trigonometric Functions Menu...")
                        msvcrt.getwch() # Press a key before returning to the main menu
                        break
            elif Option == 3:
                index2 = 0
                os.system("cls") # Clear the window
                while(index2 == 0):
                    # --------------------------------------------------- #
                    # ----- Hiperbolic Trigonometric Functions Menu ----- #
                    # --------------------------------------------------- #
                    Option = int(input("III. HIPERBOLIC TRIGONOMETRIC FUNCTIONS\n   1. sinh(x)\n   2. cosh(x)\n   3. tanh(x)\n   4. Return\n\nPlease, select an option: "))
                    if Option == 1:
                        print("Pending...")
                    elif Option == 2:
                        print("Pending...")
                    elif Option == 3:
                        print("Pending...")
                    elif Option == 4:
                        print("Press any Key to return to the Trigonometric Functions Menu...")
                        msvcrt.getwch() # Press a key before returning to the main menu
                        break
            elif Option == 4:
                print("Press any Key to return to the Main Menu...")
                msvcrt.getwch() # Press a key before returning to the main menu
                break
        os.system("cls") # Clear the window

    elif(Option == 4):
        print("Thanks for using this program! See ya soon! n.n/")
        msvcrt.getwch() # Press a key to close the program
        sys.exit() # Close the window

    else:
        print("Please, select a valid option...")
        print("Press any key to try again :)")
        msvcrt.getwch() # Press a key before returning to the main menu
        index = 1