# ---------------------- #
# ----- Libraries  ----- #
# ---------------------- #
import math
import os # "Various Operating System Interfaces" Consists mainly of functions for creating and managing running processes or file system content (files and directories).
import sys # System-specific parameters and functions
import msvcrt # Library will help to detect a key
                                    # --------------------------------- #
                                    # ----- Basic Math Functions  ----- #
                                    # --------------------------------- #
# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Addition"
class Addition():
    # Class constructor
    # def __init__(self, Num1, Num2):
    #     self.Num1 = Num1
    #     self.Num2 = Num2

    # Class method
    def AddOp(self, Num1, Num2):
        AddResult = (Num1 + Num2)
        return AddResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Substraction"
class Substraction():
    # Class constructor
    # def __init__(self, Num1, Num2):
    #     self.Num1 = Num1
    #     self.Num2 = Num2
    
    # Class method
    def SubsOp(self, Num1, Num2):
        SubsResult = (Num1 - Num2)
        return SubsResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Multiplication"
class Multiplication():
    # Class constructor
    # def __init__(self, Num1, Num2):
    #     self.Num1 = Num1
    #     self.Num2 = Num2
    
    # Class method
    def MultOp(self, Num1, Num2):
        MultResult = (Num1 * Num2)
        return MultResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Division"
class Division():
    # Class constructor
    # def __init__(self, Num1, Num2):
    #     self.Num1 = Num1
    #     self.Num2 = Num2
    
    # Class method
    def DivOp(self, Num1, Num2):
        DivResult = (Num1 / Num2)
        return DivResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Square_Root"
class Square_Root():
    # Class constructor
    # def __init__(self, Num1):
    #     self.Num1 = Num1

    # Class method
    def SquRootOp(self, Num1):
        Num1 = Num1 * 1.0
        x = Num1
        i = 0
        while i != x:
            i = x
            x = (Num1 / x + x) / 2

        SqrRResult = x # Variable "Res_SquR" is assigned "x" value
        return SqrRResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Cube_Root"
class Cube_Root():
    # Class constructor
    # def __init__(self, Num1):
    #     self.Num1 = Num1

    # Class method
    def CubeRootOp(self, Num1):
        CubeRootResult = Num1 ** (1/3)
        return CubeRootResult # Value returned

                                    # -------------------------------- #
                                    # ----- More Math Functions  ----- #
                                    # -------------------------------- #
# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Num_Squr"
class Num_Squr():
    # Class constructor
    # def __init__(self, Num1):
    #     self.Num1 = Num1
    
    # Class method
    def NumSqurOp(self, Num1):
        NumSqurResult = Num1 * Num1
        return NumSqurResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Num_Cubed"
class Num_Cubed():
    # Class constructor
    # def __init__(self, Num1):
    #     self.Num1 = Num1
    
    # Class method
    def NumCubedOp(self, Num1):
        NumCubedResult = Num1 * Num1 * Num1
        return NumCubedResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Num_Raised"
class Num_Raisedx():
    # Class constructor
    # def __init__(self, Num1, Num2):
    #     self.Num1 = Num1
    #     self.Num2 = Num2
    
    # Class method
    def NumRaisedXOp(self, Num1, Num2):
        NumRaisedXResult = Num1 ** (Num2)
        return NumRaisedXResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Num_Neg1"
class Num_Neg1():
    # Class constructor
    # def __init__(self, Num1):
    #     self.Num1 = Num1
    
    # Class method
    def NumNeg1Op(self, Num1):
        NumCNeg1Result = 1 / Num1
        return NumCNeg1Result # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Num_Neg1"
class Percentage():
    # Class constructor
    # def __init__(self, Num1):
    #     self.Num1 = Num1
    
    # Class method
    def PercentageOp(self, Num1):
        PercentageResult = Num1 / 100
        return PercentageResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Factorial"
class Factorial():
    # Class constructor
    # def __init__(self, Num1):
    #     self.Num1 = Num1

    # Class method
    def FactorialOp(self, Num1):
        FactorialResult = 1
        for i in range(1, Num1 + 1):
            FactorialResult = FactorialResult * i
        return FactorialResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Logarithm"
class Logarithm():
    # Class constructor
    # def __init__(self, Num1):
    #     self.Num1 = Num1

    # Class method
    def LogarithmOp(self, Num1):
        x = (Num1 - 1) / (Num1 + 1)
        A = (x * x) * ((1 / 3) + (1 / 5) * (x * x))

        LogarithmResult = 0.87 * x * (A + 1)
        return LogarithmResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Natural Logarithm"
class Natural_Logarithm():
    # Class constructor
    # def __init__(self, Num1):
    #     self.Num1 = Num1

    # Class method
    def NaturalLogarithmOp(self, Num1):
        x = (Num1 - 1) / (Num1 + 1)
        A = (x * x) * ((1 / 3) + (1 / 5) * (x * x))

        NatLogarithmResult = 0.87 * x * (A + 1) * 2.4025
        return NatLogarithmResult # Value returned

                                # ------------------------------------ #
                                # ----- Trigonometric Functions  ----- #
                                # ------------------------------------ #
# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Sine"
class Sine():
    # Class constructor
    # def __init__(self, Num1):
    #     self.Num1 = Num1

    # Class method
    def SineOp(self, Num1):
        SineResult = 0
        for i in range(0, 21): # Principal summation
            Dividend = 1
            for j in range((2 * i) + 1): # Dividend
                Dividend *= Num1

            Divider = 1
            for j in range(1, ((2 * i) + 1) + 1): # Divider
                Divider *= j
            
            if i % 2 == 0:
                sig = 1
            else:
                sig = -1
            
            SineResult += (Dividend / Divider) * sig
        
        return SineResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Cosine"
class Cosine():
    # Class constructor
    # def __init__(self, Num1):
    #     self.Num1 = Num1

    # Class method
    def CosineOp(self, Num1):
        CosineResult = 0
        for i in range(0, 21): # Principal summation
            Dividend = 1
            for j in range(2 * i): # Dividend
                Dividend *= Num1

            Divider = 1
            for j in range(2, ((2 * i)) + 1): # Divider
                Divider *= j
            
            if i % 2 == 0:
                sig = -1
            else:
                sig = 1
            
            CosineResult -= (Dividend / Divider) * sig
        
        return CosineResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Sineh"
class Sineh():
    # Class constructor
    # def __init__(self, Num1):
    #     self.Num1 = Num1
    
    # Class method
    def SinehOp(self, Num1):
        SinehResult = 0
        for i in range(0, 21): # Principal summation
            Dividend = 1
            for j in range((2 * i) + 1): # Dividend
                Dividend *= Num1

            Divider = 1
            for j in range(1, ((2 * i) + 1) + 1): # Divider
                Divider *= j
            
            SinehResult += (Dividend / Divider)
        
        return SinehResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Cosineh"
class Cosineh():
    # Class constructor
    # def __init__(self, Num1):
    #     self.Num1 = Num1
    
    # Class method
    def CosinehOp(self, Num1):
        CosinehResult = 0
        for i in range(0, 21): # Principal summation
            Dividend = 1
            for j in range(2 * i): # Dividend
                Dividend *= Num1

            Divider = 1
            for j in range(2, ((2 * i)) + 1): # Divider
                Divider *= j
            
            CosinehResult += (Dividend / Divider)
        
        return CosinehResult # Value returned

                                # ----------------------------------- #
                                # ----- Operations with Arrays  ----- #
                                # ----------------------------------- #
# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "CaptureArray1"
class CaptureArrays():
    # Class constructor
    # def __init__(self, n1, m1, n2, m2):
    #     self.n1 = n1
    #     self.m1 = m1
    #     self.n2 = n2
    #     self.m2 = m2
    
    # Class method #1
    def createArray1(self, n1, m1):
        Array1 = [] # Declaration of an array
        print("\n-------------------------------------------")
        print("----- Capture of numbers for Array #1 -----")
        print("-------------------------------------------")

        for i in range(n1): # Rows
            Array1.append([])
            for j in range(m1): # Columns
                value = int(input("Value [{}, {}]: ".format(i + 1, j + 1))) # Format
                Array1[i].append(value)

        print("\nTHE ARRAY #1 IS: ")
        for n1 in Array1:
            print("[", end = " ")
            for element in n1:
                print("{:2.0f}".format(element), end = " ")
            print("]")

        return Array1 # Value returned

    # Class method #2
    def createArray2(self, n2, m2):
        Array2 = [] # Declaration of an array
        print("\n-------------------------------------------")
        print("----- Capture of numbers for Array #2 -----")
        print("-------------------------------------------")

        for k in range(n2): # Rows
            Array2.append([])
            for l in range(m2): # Columns
                value = int(input("Value [{}, {}]: ".format(k + 1, l + 1))) # Format
                Array2[k].append(value)

        print("\nTHE ARRAY #2 IS: ")
        for n2 in Array2:
            print("[", end = " ")
            for element in n2:
                print("{:2.0f}".format(element), end = " ")
            print("]")

        return Array2 # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "ArrayAddition"
class ArrayAddition():
    # Class constructor
    # def __init__(self, Array1, Array2):
    #     self.Array1 = Array1
    #     self.Array2 = Array2

    # Class method
    def ArrayAdditionOp(self, Array1, Array2):
        Array3 = [] # Declaration of an array to acumulate the result of the Addition
        
        for i in range(len(Array1)):
            Array3.append([])
            for j in range(len(Array1[0])):
                Array3[i].append(Array1[i][j] + Array2[i][j])
        
        print("\nThe result of the addition for the Array 1 and 2 is: ")
        for row in Array3:
            print("[", end = " ")
            for element in row:
                print("{:2.0f}".format(element), end = " ")
            print("]")

        return Array3 # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "ArraySubstracion"
class ArraySubstracion():
    # Class constructor
    # def __init__(self, Array1, Array2):
    #     self.Array1 = Array1
    #     self.Array2 = Array2
    
    # Class method
    def ArraySubstracionOp(self, Array1, Array2):
        Array3 = [] # Declaration of an array to acumulate the result of the Substraction
        
        for i in range(len(Array1)):
            Array3.append([])
            for j in range(len(Array1[0])):
                Array3[i].append(Array1[i][j] - Array2[i][j])
        
        print("\nThe result of the substraction for the Array 1 and 2 is: ")
        for row in Array3:
            print("[", end = " ")
            for element in row:
                print("{:2.0f}".format(element), end = " ")
            print("]")

        return Array3 # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "ArrayMultiplication"
class ArrayMultiplication():
    # Class constructor
    # def __init__(self, Array1, Array2):
    #     self.Array1 = Array1
    #     self.Array2 = Array2
    
    # Class method
    def ArrayMultiplicationOp(self, Array1, Array2):
        Array3 = [] # Declaration of an array to acumulate the result of the Multiplication

        # Creation of an array of ceros
        for i in range(len(Array1)):
            Array3.append([])
            for j in range(len(Array2[0])):
                Array3[i].append(0)

        for i in range(len(Array1)):
            for j in range(len(Array2[0])):
                for k in range(len(Array1[0])):
                    Array3[i][j] += Array1[i][k] * Array2[k][j]
        
        print("\nThe result of the multiplication for the Array 1 and 2 is: ")
        for row in Array3:
            print("[", end = " ")
            for element in row:
                print("{:2.0f}".format(element), end = " ")
            print("]")

        return Array3 # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "ArrayMultScalar"
class ArrayMultScalar():
    # Class constructor
    # def __init__(self, Array, Scalar):
    #     self.Array = Array
    #     self.Scalar = Scalar
    
    # Class method
    def ArrayMultScalarOp(self, Array, Scalar):
        Array3 = [] # Declaration of an array to acumulate the Multiplication

        # Creation of an array of ceros
        for i in range(len(Array)):
            Array3.append([])
            for j in range(len(Array[0])):
                Array3[i].append(Array[i][j] * Scalar)
        
        print("The result of the multiplication of the array with a scalar is: ")
        for row in Array3:
            print("[", end = " ")
            for element in row:
                print("{:2.0f}".format(element), end = " ")
            print("]")

        return Array3 # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "ArrayTransposed"
class ArrayTransposed():
    # Class constructor
    # def __init__(self, Array):
    #     self.Array = Array
    
    # Class method
    def ArrayTransposedOp(self, Array):
        Array3 = [] # Declaration of an array to acumulate the Transposed array

        # Creation of an array of ceros
        for i in range(len(Array)):
            Array3.append([])
            for j in range(len(Array[0])):
                Array3[i].append(Array[j][i])
        
        print("The result of the transpose of the array: ")
        for row in Array3:
            print("[", end = " ")
            for element in row:
                print("{:2.0f}".format(element), end = " ")
            print("]")

        return Array3 # Value returned

                                # ---------------------------- #
                                # ----- Other funcrions  ----- #
                                # ---------------------------- #
# ------------------------------------------------------------------------------------------------------------ #
def ReadKey():
    print("\nPress any Key to return to the previos Menu...")
    msvcrt.getwch() # Press a key before returning to the previos Menu
    os.system("cls") # Clear the window                           