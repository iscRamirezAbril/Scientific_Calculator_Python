import math
                                    # --------------------------------- #
                                    # ----- Basic Math Functions  ----- #
                                    # --------------------------------- #
# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Addition"
class Addition():
    # Class constructor
    def __init__(self, Num1, Num2):
        self.Num1 = Num1
        self.Num2 = Num2

    # Class method
    def AddOp(self, Num1, Num2):
        AddResult = (Num1 + Num2)
        return AddResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Substraction"
class Substraction():
    # Class constructor
    def __init__(self, Num1, Num2):
        self.Num1 = Num1
        self.Num2 = Num2
    
    # Class method
    def SubsOp(self, Num1, Num2):
        SubsResult = (Num1 - Num2)
        return SubsResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Multiplication"
class Multiplication():
    # Class constructor
    def __init__(self, Num1, Num2):
        self.Num1 = Num1
        self.Num2 = Num2
    
    # Class method
    def MultOp(self, Num1, Num2):
        MultResult = (Num1 * Num2)
        return MultResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Division"
class Division():
    # Class constructor
    def __init__(self, Num1, Num2):
        self.Num1 = Num1
        self.Num2 = Num2
    
    # Class method
    def DivOp(self, Num1, Num2):
        DivResult = (Num1 / Num2)
        return DivResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Square_Root"
class Square_Root():
    # Class constructor
    def __init__(self, Num1):
        self.Num1 = Num1

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
    def __init__(self, Num1):
        self.Num1 = Num1

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
    def __init__(self, Num1):
        self.Num1 = Num1
    
    # Class method
    def NumSqurOp(self, Num1):
        NumSqurResult = Num1 * Num1
        return NumSqurResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Num_Cubed"
class Num_Cubed():
    # Class constructor
    def __init__(self, Num1):
        self.Num1 = Num1
    
    # Class method
    def NumCubedOp(self, Num1):
        NumCubedResult = Num1 * Num1 * Num1
        return NumCubedResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Num_Raised"
class Num_Raisedx():
    # Class constructor
    def __init__(self, Num1, Num2):
        self.Num1 = Num1
        self.Num2 = Num2
    
    # Class method
    def NumRaisedXOp(self, Num1, Num2):
        NumRaisedXResult = Num1 ** (Num2)
        return NumRaisedXResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Num_Neg1"
class Num_Neg1():
    # Class constructor
    def __init__(self, Num1):
        self.Num1 = Num1
    
    # Class method
    def NumNeg1Op(self, Num1):
        NumCNeg1Result = 1 / Num1
        return NumCNeg1Result # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Num_Neg1"
class Percentage():
    # Class constructor
    def __init__(self, Num1):
        self.Num1 = Num1
    
    # Class method
    def PercentageOp(self, Num1):
        PercentageResult = Num1 / 100
        return PercentageResult # Value returned

# ------------------------------------------------------------------------------------------------------------ #
# Creation of a class called "Factorial"
class Factorial():
    # Class constructor
    def __init__(self, Num1):
        self.Num1 = Num1

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
    def __init__(self, Num1):
        self.Num1 = Num1

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
    def __init__(self, Num1):
        self.Num1 = Num1

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
    def __init__(self, Num1):
        self.Num1 = Num1

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
    def __init__(self, Num1):
        self.Num1 = Num1

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
