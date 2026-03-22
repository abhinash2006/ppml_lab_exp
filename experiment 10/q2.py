class Add:
    def add(self, a, b):
        return a + b

class Subtract:
    def subst(self, a, b):
        return a - b

class Multiply:
    def mult(self, a, b):
        return a * b

class Division:
    def division(self, a, b):
        if b != 0:
            return a / b
        return "Cannot divide by zero"

class Calculator(Add, Subtract, Multiply, Division):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
    
    def perform_operations(self):
        print("Addition:", self.add(self.data1, self.data2))
        print("Subtraction:", self.subst(self.data1, self.data2))
        print("Multiplication:", self.mult(self.data1, self.data2))
        print("Division:", self.division(self.data1, self.data2))

calc = Calculator(10, 5)
calc.perform_operations()
