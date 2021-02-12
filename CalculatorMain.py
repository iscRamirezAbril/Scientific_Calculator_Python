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

    Option = int(input("This is the Principal Menu\n   1. Basic Math Functions\n   2. More Math Functions\n   3. Trigonometric Functions\n   4. Operations with Arrays\n   5. Exit\n\nPlease, select an option: "))

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
            Option = int(input("C. TRIGONOMETRIC FUNCTIONS\n   1. Basic Trigonometric Functions\n   2. Hiperbolic Trigonometric Functions\n   3. Return\n\nPlease, select an option: "))
            
            # Option to enter to the "Basic Trigonometric Functions" Menu
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

                        objSine = Sine(Num1) # Creation of an object from the class "Sine"
                        objCosine = Cosine(Num1) # Creation of an object from the class "Cosine"

                        TangentResult = objSine.SineOp(Num1) / objCosine.CosineOp(Num1) # Method call
                        print("\nTHE TANGENT [IN RADIANS] IS: " + str(TangentResult)) # Result

                        print("\nPress any Key to return to the Basic Trigonometric Functions...")
                        msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                        os.system("cls") # Clear the window

                    # Option to calculate the "Secant(x)" of a number
                    elif Option == 4:
                        Num1 = float(input("- Insert a number to calculate it Secant(x): "))

                        objSine = Sine(Num1) # Creation of an object from the class "Sine"
                        objCosine = Cosine(Num1) # Creation of an object from the class "Cosine"

                        SecantResult = objSine.SineOp(Num1) / objCosine.CosineOp(Num1) # Method call
                        print("\nTHE SECANT [IN RADIANS] IS: " + str(SecantResult)) # Result

                        print("\nPress any Key to return to the Basic Trigonometric Functions...")
                        msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                        os.system("cls") # Clear the window

                    # Option to calculate the "Cosecant(x)" of a number
                    elif Option == 5:
                        Num1 = float(input("- Insert a number to calculate it Cosecant(x): "))

                        objSine = Sine(Num1) # Creation of an object from the class "Sine"
                        objCosine = Cosine(Num1) # Creation of an object from the class "Cosine"

                        CotangentResult = objCosine.CosineOp(Num1) / objSine.SineOp(Num1) # Method call
                        CosecantResult = CotangentResult / objCosine.CosineOp(Num1)
                        print("\nTHE COSECANT [IN RADIANS] IS: " + str(CosecantResult)) # Result

                        print("\nPress any Key to return to the Basic Trigonometric Functions...")
                        msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                        os.system("cls") # Clear the window

                    # Option to calculate the "Cotangent(x)" of a number
                    elif Option == 6:
                        Num1 = float(input("- Insert a number to calculate it Cosecant(x): "))

                        objSine = Sine(Num1) # Creation of an object from the class "Sine"
                        objCosine = Cosine(Num1) # Creation of an object from the class "Cosine"

                        CotangentResult = objCosine.CosineOp(Num1) / objSine.SineOp(Num1) # Method call

                        print("\nTHE COTANGENT [IN RADIANS] IS: " + str(CotangentResult)) # Result

                        print("\nPress any Key to return to the Basic Trigonometric Functions...")
                        msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                        os.system("cls") # Clear the window

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

            # Option to enter to the "Hiperbolic Trigonometric Functions" Menu
            elif Option == 2:
                index2 = 0
                os.system("cls") # Clear the window
                while(index2 == 0):
                    # --------------------------------------------------- #
                    # ----- Hiperbolic Trigonometric Functions Menu ----- #
                    # --------------------------------------------------- #
                    Option = int(input("II. HIPERBOLIC TRIGONOMETRIC FUNCTIONS\n   1. sinh(x)\n   2. cosh(x)\n   3. tanh(x)\n   4. csch(x)\n   5. sech(x)\n   6. coth(x)\n   7. Return\n\nPlease, select an option: "))
                    
                    # Option to calculate the "Sineh(x)" of a number
                    if Option == 1:
                        Num1 = float(input("- Insert a number to calculate it Sineh(x): "))

                        objSineh = Sineh(Num1) # Creation of an object from the class "Sineh"

                        SinehResult = objSineh.SinehOp(Num1) # Method call

                        print("\nTHE HIPERBOLIC SINE [IN DEGREES] IS: " + str(SinehResult)) # Result

                        print("\nPress any Key to return to the Basic Trigonometric Functions...")
                        msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                        os.system("cls") # Clear the window

                   # Option to calculate the "Cosineh(x)" of a number
                    elif Option == 2:
                        Num1 = float(input("- Insert a number to calculate it Cosineh(x): "))

                        objCosineh = Cosineh(Num1) # Creation of an object from the class "Cosineh"

                        CosinehResult = objCosineh.CosinehOp(Num1) # Method call

                        print("\nTHE HIPERBOLIC COSINE [IN DEGREES] IS: " + str(CosinehResult)) # Result

                        print("\nPress any Key to return to the Basic Trigonometric Functions...")
                        msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                        os.system("cls") # Clear the window

                   # Option to calculate the "Tangenth(x)" of a number
                    elif Option == 3:
                        Num1 = float(input("- Insert a number to calculate it Tangenth(x): "))

                        objSineh = Sineh(Num1) # Creation of an object from the class "Sineh"
                        objCosineh = Cosineh(Num1) # Creation of an object from the class "Cosineh"

                        TangenthResult = objSineh.SinehOp(Num1) / objCosineh.CosinehOp(Num1) # Method call

                        print("\nTHE HIPERBOLIC TANGENT [IN DEGREES] IS: " + str(TangenthResult)) # Result

                        print("\nPress any Key to return to the Basic Trigonometric Functions...")
                        msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                        os.system("cls") # Clear the window

                    # Option to calculate the "Cosecanth(x)" of a number
                    elif Option == 4:
                        Num1 = float(input("- Insert a number to calculate it Cosecanth(x): "))

                        objSineh = Sineh(Num1) # Creation of an object from the class "Sineh"

                        CosecanthResult = 1 / objSineh.SinehOp(Num1) # Method call

                        print("\nTHE HIPERBOLIC COSECANT [IN DEGREES] IS: " + str(CosecanthResult)) # Result

                        print("\nPress any Key to return to the Basic Trigonometric Functions...")
                        msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                        os.system("cls") # Clear the window

                    # Option to calculate the "Secanth(x)" of a number
                    elif Option == 5:
                        Num1 = float(input("- Insert a number to calculate it Secanth(x): "))

                        objCosineh = Cosineh(Num1) # Creation of an object from the class "Cosineh"

                        SecanthResult = 1 / objCosineh.CosinehOp(Num1) # Method call

                        print("\nTHE HIPERBOLIC SECANT [IN DEGREES] IS: " + str(SecanthResult)) # Result

                        print("\nPress any Key to return to the Basic Trigonometric Functions...")
                        msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                        os.system("cls") # Clear the window

                    # Option to calculate the "Cotangenth(x)" of a number
                    elif Option == 6:
                        Num1 = float(input("- Insert a number to calculate it Cotangenth(x): "))

                        objSineh = Sineh(Num1) # Creation of an object from the class "Sineh"
                        objCosineh = Cosineh(Num1) # Creation of an object from the class "Cosineh"

                        TangenthResult = objSineh.SinehOp(Num1) / objCosineh.CosinehOp(Num1) # Method call
                        ContangenthResult = 1 / TangenthResult

                        print("\nTHE HIPERBOLIC COTANGENT [IN DEGREES] IS: " + str(ContangenthResult)) # Result

                        print("\nPress any Key to return to the Basic Trigonometric Functions...")
                        msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                        os.system("cls") # Clear the window

                    # Option to return to the Main Menu
                    elif Option == 7:
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

            elif Option == 3:
                print("Press any Key to return to the Main Menu...")
                msvcrt.getwch() # Press a key before returning to the main menu
                break
        os.system("cls") # Clear the window

    # Option to enter to the "Operations with Arrays" Menu
    elif Option == 4:
        index2 = 0
        os.system("cls") # Clear the window
        print("----- CAPTURE OF THE ARRAYS -----")
        print("For some operations, you need to capture 2 arrays...")
        print("\n----- First Array -----")
        n1 = int(input("  - Please, insert the number of rows that you want in the Array #1: "))
        m1 = int(input("  - Please, insert the number of columns that you want in the Array #1: "))

        print("\n----- Second Array -----")
        n2 = int(input("  - Please, insert the number of rows that you want in the Array #2: "))
        m2 = int(input("  - Please, insert the number of columns that you want in the Array #2: "))
        objArrayCapture = CaptureArrays(n1, m1, n2, m2) # Creation of an object from the class "CaptureArrays"
        
        Array1 = objArrayCapture.createArray1(n1, m1) # Method call and result
        Array2 = objArrayCapture.createArray2(n2, m2) # Method call and result
        
        print("\nPress any Key to enter to the Operations with Arrays Menu...")
        msvcrt.getwch() # Press a key before returning to the More Math Functions Menu

        while(index2 == 0):
            # --------------------------------------- #
            # ----- Operations with Arrays Menu ----- #
            # --------------------------------------- #
            Option = int(input("\nIII. OPERATIONS WITH ARRAYS\n   1. Addition\n   2. Substraction\n   3. Multiplication\n   4. Multiplication of an array with scalar\n   5. Transpose of an array\n   6. Return\n\nPlease, select an option: "))
            
            # Option to calculate the "Addition" of 2 arrays
            if Option == 1:
                if len(Array1) == len(Array2) and len(Array1[0]) == len(Array2[0]):
                    print("\n----- ADDITION  -----")
                    objArrayAdd = ArrayAddition(Array1, Array2) # Creation of an object from the class "ArrayAddition"
                    Array3 = objArrayAdd.ArrayAdditionOp(Array1, Array2) # Method call and result

                else:
                    print("The addition of the Arrays can´t be calculate because both of them have different lengths...")

                print("\nPress any Key to return to the Operations with Arrays Menu...")
                msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                os.system("cls") # Clear the window

            # Option to calculate the "Substraction" of 2 arrays
            elif Option == 2:
                if len(Array1) == len(Array2) and len(Array1[0]) == len(Array2[0]):
                    print("\n----- SUBSTRACTION -----")
                    objArraySubs = ArraySubstracion(Array1, Array2) # Creation of an object from the class "ArraySubstraction"
                    Array3 = objArraySubs.ArraySubstracionOp(Array1, Array2) # Method call and result
                
                else:
                    print("The substraction of the Arrays can´t be calculate because both of them have different lengths...")
                
                print("\nPress any Key to return to the Operations with Arrays Menu...")
                msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                os.system("cls") # Clear the window

            # Option to calculate the "Multiplication" of 2 arrays
            elif Option == 3:
                print("\n----- MULTIPLICATION -----")
                objArrayMult = ArrayMultiplication(Array1, Array2) # Creation of an object from the class "ArrayMultiplication"
                Array3 = objArrayMult.ArrayMultiplicationOp(Array1, Array2) # Method call and result

                print("\nPress any Key to return to the Operations with Arrays Menu...")
                msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                os.system("cls") # Clear the window

            # Option to calculate the "Multiplication of an array with scalar"
            elif Option == 4:
                Option = int(input("Which Array want to multiplicate with scalar? (1 / 2): "))

                # If the option is 1
                if Option == 1:
                    print("\n----- MULTIPLICATION OF AN ARRAY WITH SCALAR -----")
                    Scalar = int(input("Please, insert the value for the scalar: "))

                    objArrayMultScalar = ArrayMultScalar(Array1, Scalar) # Creation of an object from the class "ArrayMultScalar"
                    Array3 = objArrayMultScalar.ArrayMultScalarOp(Array1, Scalar) # Method call and result

                # If the option is 2
                elif Option == 2:
                    print("\n----- MULTIPLICATION OF AN ARRAY WITH SCALAR -----")
                    Scalar = int(input("Please, insert the value for the scalar: "))

                    objArrayMultScalar = ArrayMultScalar(Array2, Scalar) # Creation of an object from the class "ArrayMultScalar"
                    Array3 = objArrayMultScalar.ArrayMultScalarOp(Array2, Scalar) # Method call and result
                
                else:
                    print("Please, insert a valid option...")

                print("\nPress any Key to return to the Operations with Arrays Menu...")
                msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                os.system("cls") # Clear the window

            # Option to calculate the "Transpose" of an array
            elif Option == 5:
                Option = int(input("Which Array want to calculate it Transpose? (1 / 2): "))

                # If the option is 1
                if Option == 1:
                    print("\n----- TRANSPOSE -----")
                    objArrayTranspose = ArrayTransposed(Array1) # Creation of an object from the class "ArrayTransposed"
                    Array3 = objArrayTranspose.ArrayTransposedOp(Array1) # Method call and result

                # If the option is 2
                elif Option == 2:
                    print("\n----- TRANSPOSE -----")
                    objArrayTranspose = ArrayTransposed(Array2) # Creation of an object from the class "ArrayTransposed"
                    Array3 = objArrayTranspose.ArrayTransposedOp(Array2) # Method call and result
                
                else:
                    print("Please, insert a valid option...")

                print("\nPress any Key to return to the Operations with Arrays Menu...")
                msvcrt.getwch() # Press a key before returning to the More Math Functions Menu
                os.system("cls") # Clear the window

            # Option to return to the Main Menu
            elif Option == 6:
                print("Press any Key to return to the Operations with Arrays Menu...")
                msvcrt.getwch() # Press a key before returning to the main menu
                break

            # If the option isn't valid
            else:
                print("\nPlease, select a valid option...")
                print("Press any key to try again :)")
                msvcrt.getwch() # Press a key before returning to the Inverse Trigonometric Functions Menu
                index1 = 0
                os.system("cls") # Clear the window

    # Close the program
    elif(Option == 5):
        print("\nThanks for using this program! See ya soon! n.n/")
        msvcrt.getwch() # Press a key to close the program
        sys.exit() # Close the window

    # If the option isn't valid
    else:
        print("\nPlease, select a valid option...")
        print("Press any key to try again :)")
        msvcrt.getwch() # Press a key before returning to the main menu
        index = 1