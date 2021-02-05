# <---------------------> #
# <----- Libraries -----> #
# <---------------------> #
import os
import sys
import msvcrt
import math
from FunctionLibrary import * # My library
from colorama import init, Fore # This is the library that will help with the text color.
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

    # Option to enter to the "Basic Math Functions" menu
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
                Num1 = float(input("- Insert the first number: "))
                Num2 = float(input("- Insert the second number: "))
                objAdd = Addition(Num1, Num2) # Creation of an object from the class "Addition"
                AddResult = objAdd.AddOp(Num1, Num2) # Method call
                print("\nTHE ANSWER OF THE ADDITION IS: " + str(AddResult)) # Result

                print("\nPress any Key to return to the Basic Math Functions...")
                msvcrt.getwch() # Press a key before returning to the Basic Math Functions Menu
                os.system("cls") # Clear the window

            # Option for "Substraction" function
            elif Option == 2:
                Num1 = float(input("- Insert the first number: "))
                Num2 = float(input("- Insert the second number: "))
                objSubs = Substraction(Num1, Num2) # Creation of an object from the class "Substraction"
                SubsResult = objSubs.SubsOp(Num1, Num2) # Method call
                print("\nTHE ANSWER OF THE SUBSTRACTION IS: " + str(SubsResult)) # Result

                print("\nPress any Key to return to the Basic Math Functions...")
                msvcrt.getwch() # Press a key before returning to the Basic Math Functions Menu
                os.system("cls") # Clear the window

            # Option for "Multiplication" function
            elif Option == 3:
                Num1 = float(input("- Insert the first number: "))
                Num2 = float(input("- Insert the second number: "))
                objMult = Multiplication(Num1, Num2) # Creation of an object from the class "Multiplication"
                MultResult = objMult.MultOp(Num1, Num2) # Method call
                print("\nTHE ANSWER OF THE MULTIPLICATION IS: " + str(MultResult)) # Result

                print("\nPress any Key to return to the Basic Math Functions...")
                msvcrt.getwch() # Press a key before returning to the Basic Math Functions Menu
                os.system("cls") # Clear the window

            # Option for "Division" function
            elif Option == 4:
                Num1 = float(input("- Insert the first number: "))
                Num2 = float(input("- Insert the second number: "))

                if Num2 == 0:
                    print("\nMATH ERROR!...")
                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the Basic Math Functions Menu
                    os.system("cls") # Clear the window
                else:
                    objDiv = Division(Num1, Num2) # Creation of an object from the class "Division"
                    DivResult = objDiv.DivOp(Num1, Num2) # Method call
                    print("\nTHE ANSWER OF THE DIVIISON IS: " + str(DivResult)) # Result

                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the Basic Math Functions Menu
                    os.system("cls") # Clear the window

            # Option for "Square Root" function
            elif Option == 5:
                Num1 = float(input("- Insert the number that you want to calculate it square root: "))

                if Num1 < 0:
                    print("\nMATH ERROR!...")
                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the Basic Math Functions Menu
                    os.system("cls") # Clear the window
                else:
                    objSqrRoot = Square_Root(Num1) # Creation of an object from the class "Square_Root"
                    SqrRootResult = objSqrRoot.SquRootOp(Num1) # Method call
                    print("\nTHE ANSWER OF THE SQUARE ROOT IS: " + str(SqrRootResult)) # Result

                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the Basic Math Functions Menu
                    os.system("cls") # Clear the window

            # Option for "Cube Root" function
            elif Option == 6:
                Num1 = float(input("- Insert the number that you want to calculate it cube root: "))

                objCubeRoot = Cube_Root(Num1) # Creation of an object from the class "Cube_Root"
                CubeRootResult = objCubeRoot.CubeRootOp(Num1) # Method call
                print("\nTHE ANSWER OF THE CUBE ROOT IS: " + str(CubeRootResult)) # Result

                print("\nPress any Key to return to the Basic Math Functions...")
                msvcrt.getwch() # Press a key before returning to the Basic Math Functions Menu
                os.system("cls") # Clear the window

            # Option to return to the main menu
            elif Option == 7:
                print("\nPress any Key to return to the Main Menu...")
                msvcrt.getwch() # Press a key before returning to the Main Menu
                break

            # If the option isn't valid
            else:
                print("\nPlease, select a valid option...")
                print("Press any key to try again :)")
                msvcrt.getwch() # Press a key before returning to the Basic Math Functions Menu
                index1 = 0
                os.system("cls") # Clear the window

    # Option to enter to the "More Math Functions" menu
    elif(Option == 2):
        index1 = 0
        os.system("cls") # Clear the window
        while(index1 == 0):
            # ------------------------------------ #
            # ----- More Math Functions Menu ----- #
            # ------------------------------------ #
            Option = int(input("B. MORE MATH FUNCTIONS\n   1. Square of a number\n   2. Cube of a number\n   3. Number Raised to x power\n   4. Number Raised to -1 power\n   5. Percentage of a number\n   6. Factorial\n   7. Logarithm\n   8. Natural Logarithm\n   9. Return\n\nPlease, select an option: "))
            
            # Option for "Square of a number" operation
            if Option == 1:
                Num1 = float(input("- Insert the number that you want to elevate at square power: "))

                objNumSqu = Num_Squr(Num1) # Creation of an object from the class "Num_Squr"
                NumSqurResult = objNumSqu.NumSqurOp(Num1) # Method call
                print("\nTHE SQUARE OF THE NUMBER IS: " + str(NumSqurResult)) # Result

                print("\nPress any Key to return to the Basic Math Functions...")
                msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                os.system("cls") # Clear the window

            # Option for "Cube of a number" operation
            elif Option == 2:
                Num1 = float(input("- Insert the number that you want to elevate at cube power: "))

                objNumCube = Num_Cubed(Num1) # Creation of an object from the class "Num_Cubed"
                NumSqurResult = objNumCube.NumCubedOp(Num1) # Method call
                print("\nTHE CUBE OF THE NUMBER IS: " + str(NumSqurResult)) # Result

                print("\nPress any Key to return to the Basic Math Functions...")
                msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                os.system("cls") # Clear the window

            # Option for "Number Raised to x power" operation   
            elif Option == 3:
                Num1 = float(input("- Insert the number that you want to elevate at x power: "))
                Num2 = float(input("- Insert the x number (the exponent): "))

                objNumRaisedX = Num_Raisedx(Num1, Num2) # Creation of an object from the class "Num_Raisedx"
                NumRaisedXResult = objNumRaisedX.NumRaisedXOp(Num1, Num2) # Method call
                print("\nTHE ANSWER IS: " + str(NumRaisedXResult)) # Result

                print("\nPress any Key to return to the Basic Math Functions...")
                msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                os.system("cls") # Clear the window

            # Option for "Number Raised to -1 power" operation
            elif Option == 4:
                Num1 = float(input("- Insert the number that you want to elevate at -1 power: "))

                objNumNeg1 = Num_Neg1(Num1) # Creation of an object from the class "Num_Neg1"
                NumNeg1Result = objNumNeg1.NumNeg1Op(Num1) # Method call
                print("\nTHE ANSWER IS: " + str(NumNeg1Result)) # Result

                print("\nPress any Key to return to the Basic Math Functions...")
                msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                os.system("cls") # Clear the window

            # Option for "Percentage of a number" operation
            elif Option == 5:
                Num1 = float(input("- Insert the number that you want to calculate it percentage: "))

                objPercentage = Percentage(Num1) # Creation of an object from the class "Percentage"
                PercentageResult = objPercentage.PercentageOp(Num1) # Method call
                print("\nTHE PERCENTAGE IS: " + str(PercentageResult)) # Result

                print("\nPress any Key to return to the Basic Math Functions...")
                msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                os.system("cls") # Clear the window

            # Option to calculate the "Factorial"
            elif Option == 6:
                Num1 = int(input("- Insert a number to calculate it factorial: "))

                if Num1 == 1:
                    print("\nTHE FACTORIAL IS: 1") # Result
                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                    os.system("cls") # Clear the window
                else:
                    objFactorial = Factorial(Num1) # Creation of an object from the class "Factorial"
                    FactorialResult = objFactorial.FactorialOp(Num1) # Method call
                    print("\nTHE FACTORIAL IS: " + str(FactorialResult)) # Result

                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                    os.system("cls") # Clear the window

            # Option to calculate the "Logarithm"
            elif Option == 7:
                Num1 = float(input("- Insert a number to calculate it Logarithm: "))

                if Num1 <= 0:
                    print("\nMATH ERROR!...")
                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                    os.system("cls") # Clear the window
                else:
                    objLogarithm = Logarithm(Num1) # Creation of an object from the class "Logarithm"
                    LogarithmResult = objLogarithm.LogarithmOp(Num1) # Method call
                    print("\nTHE LOGARITHM IS: " + str(LogarithmResult)) # Result

                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                    os.system("cls") # Clear the window

            # Option to calculate the "Natural Logarithm"
            elif Option == 8:
                Num1 = float(input("- Insert a number to calculate it Natural Logarithm: "))

                if Num1 <= 0:
                    print("\nMATH ERROR!...")
                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                    os.system("cls") # Clear the window
                else:
                    objNatLogarithm = Natural_Logarithm(Num1) # Creation of an object from the class "Natural_Logarithm"
                    NaturalLogarithmResult = objNatLogarithm.NaturalLogarithmOp(Num1) # Method call
                    print("\nTHE NATURAL LOGARITHM IS: " + str(NaturalLogarithmResult)) # Result

                    print("\nPress any Key to return to the Basic Math Functions...")
                    msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                    os.system("cls") # Clear the window

            # Option to return to the Main Menu
            elif Option == 9:
                print("\nPress any Key to return to the Main Menu...")
                msvcrt.getwch() # Press a key before returning to the Main Menu
                break

            # If the option isn't valid
            else:
                print("\nPlease, select a valid option...")
                print("Press any key to try again :)")
                msvcrt.getwch() # Press a key before returning to the Basic Math Functions Menu
                index1 = 0
                os.system("cls") # Clear the window

    # Option to enter to the "Trigonometric Functions" menu
    elif(Option == 3):
        index1 = 0
        os.system("cls") # Clear the window
        while(index1 == 0):
            os.system("cls") # Clear the window
            # ---------------------------------------- #
            # ----- Trigonometric Functions Menu ----- #
            # ---------------------------------------- #
            Option = int(input("C. TRIGONOMETRIC FUNCTIONS\n   1. Basic Trigonometric Functions\n   2. Inverse Trigonometric Functions\n   3. Hiperbolic Trigonometric Functions\n   4. Return\n\nPlease, select an option: "))
            
            # Option to enter to the "Basic Math Functions" Menu
            if Option == 1:
                index2 = 0
                os.system("cls") # Clear the window
                while(index2 == 0):
                    # ---------------------------------------------- #
                    # ----- Basic Trigonometric Functions Menu ----- #
                    # ---------------------------------------------- #
                    Option = int(input("I. BASIC TRIGONOMETRIC FUNCTIONS\n   1. Sine [sin(x)]\n   2. Cosine [cos(x)]\n   3. Tangent [tan(x)]\n   4. Secant [sec(x)]\n   5. Cosecant [csc(x)]\n   6. Cotangent [cot[x]]\n   7. Return\n\nPlease, select an option: "))
                    
                    # Option to calculate the "Sine(x)" of a number
                    if Option == 1:
                        Num1 = float(input("- Insert a number to calculate it Sine(x): "))

                        objSine = Sine(Num1) # Creation of an object from the class "Sine"
                        SineResult = objSine.SineOp(Num1) # Method call
                        print("\nTHE SINE [IN RADIANS] IS: " + str(SineResult)) # Result

                        print("\nPress any Key to return to the Basic Trigonometric Functions...")
                        msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                        os.system("cls") # Clear the window

                    # Option to calculate the "Cosine(x)" of a number
                    elif Option == 2:
                        Num1 = float(input("- Insert a number to calculate it Cosine(x): "))

                        objCosine = Cosine(Num1) # Creation of an object from the class "Cosine"
                        CosineResult = objCosine.CosineOp(Num1) # Method call
                        print("\nTHE COSINE [IN RADIANS] IS: " + str(CosineResult)) # Result

                        print("\nPress any Key to return to the Basic Trigonometric Functions...")
                        msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                        os.system("cls") # Clear the window

                    # Option to calculate the "Tangent(x)" of a number
                    elif Option == 3:
                        Num1 = float(input("- Insert a number to calculate it Tangent(x): "))

                    elif Option == 4:
                        print("Pending...")
                    elif Option == 5:
                        print("Pending...")
                    elif Option == 6:
                        print("Pending...")

                    # Option to return to the Main Menu
                    elif Option == 7:
                        print("Press any Key to return to the Trigonometric Functions Menu...")
                        msvcrt.getwch() # Press a key before returning to the Trigonometric Functions Menu
                        break

                    # If the option isn't valid
                    else:
                        print("\nPlease, select a valid option...")
                        print("Press any key to try again :)")
                        msvcrt.getwch() # Press a key before returning to the Basic Math Functions Menu
                        index1 = 0
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

                    # If the option isn't valid
                    else:
                        print("\nPlease, select a valid option...")
                        print("Press any key to try again :)")
                        msvcrt.getwch() # Press a key before returning to the Inverse Trigonometric Functions Menu
                        index1 = 0
                        os.system("cls") # Clear the window

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

                    # If the option isn't valid
                    else:
                        print("\nPlease, select a valid option...")
                        print("Press any key to try again :)")
                        msvcrt.getwch() # Press a key before returning to the Hiberbolic Trigonometric Functions Menu
                        index1 = 0
                        os.system("cls") # Clear the window

            elif Option == 4:
                print("Press any Key to return to the Main Menu...")
                msvcrt.getwch() # Press a key before returning to the main menu
                break
        os.system("cls") # Clear the window

    # Close the program
    elif(Option == 4):
        print("\nThanks for using this program! See ya soon! n.n/")
        msvcrt.getwch() # Press a key to close the program
        sys.exit() # Close the window

    # If the option isn't valid
    else:
        print("\nPlease, select a valid option...")
        print("Press any key to try again :)")
        msvcrt.getwch() # Press a key before returning to the main menu
        index = 1