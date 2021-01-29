# Creation of a class called "Addition"
class Addition():
    # Class constructor
    def __init__(self, Num1, Num2):
        self.Num1 = Num1
        self.Num2 = Num2

    # Class method
    def AddOp(self, Num1, Num2):
        AddResult = (Num1 + Num2)
        return AddResult

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
        return SubsResult
# -------------------------------------------------------------------------------------------------------------#

class Multiplication():
    # Class constructor
    def __init__(self, Num1, Num2):
        self.Num1 = Num1
        self.Num2 = Num2
    
    # Class method
    def MultOp(self, Num1, Num2):
        MultResult = (Num1 * Num2)
        return MultResult

# -------------------------------------------------------------------------------------------------------------#

class Division():
    # Class constructor
    def __init__(self, Num1, Num2):
        self.Num1 = Num1
        self.Num2 = Num2
    
    # Class method
    def DivOp(self, Num1, Num2):
        DivResult = (Num1 / Num2)
        return DivResult
