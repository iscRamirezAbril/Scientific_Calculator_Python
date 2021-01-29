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

# ------------------------------------------------------------------------------------------------------------#
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
# -------------------------------------------------------------------------------------------------------------#
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

# -------------------------------------------------------------------------------------------------------------#
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

# -------------------------------------------------------------------------------------------------------------#
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

# -------------------------------------------------------------------------------------------------------------#
# Creation of a class called "Cube_Root"
class Cube_Root():
    # Class constructor
    def __init__(self, Num1):
        self.Num1 = Num1

    # Class method
    def CubeRootOp(self, Num1):
        CubeRootResult = Num1 ** (1/3)
        return CubeRootResult # Value returned

# -------------------------------------------------------------------------------------------------------------#
# Creation of a class called "Num_Squr"
class Num_Squr():
    # Class constructor
    def __init__(self, Num1):
        self.Num1 = Num1
    
    # Class method
    def NumSqurOp(self, Num1):
        NumSqurResult = Num1 * Num1
        return NumSqurResult # Value returned

# -------------------------------------------------------------------------------------------------------------#
# Creation of a class called "Num_Cubed"
class Num_Cubed():
    # Class constructor
    def __init__(self, Num1):
        self.Num1 = Num1
    
    # Class method
    def NumCubedOp(self, Num1):
        NumCubedResult = Num1 * Num1 * Num1
        return NumCubedResult # Value returned

# -------------------------------------------------------------------------------------------------------------#
# Creation of a class called "Num_Cubed"
class Num_Raisedx():
    # Class constructor
    def __init__(self, Num1, Num2):
        self.Num1 = Num1
        self.Num2 = Num2
    
    # Class method
    def NumRaisedXOp(self, Num1, Num2):
        NumRaisedXResult = Num1 ** (Num2)
        return NumRaisedXResult # Value returned