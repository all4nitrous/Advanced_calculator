#from calculator.operationd import add, subtract, multiply, divide

class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation  = operation
"""Allows operations between a & b"""
def get_result(self):
    return self.operation(self.a, self.b)


'''Add function'''
def add(a,b):
    calculation = Calculation(a, b, add)
    return calculation.get.result()

'''Subtract Function'''
def subtract(a,b):
    calculation = Calculation(a, b, subtract)
    return calculation.get.result()

'''Multiplication Function'''
def multiply(a,b):
    calculation = Calculation(a, b, multiply)
    return calculation.get.result()

'''Division Function'''
def divide(a,b):
    calculation = Calculation(a, b, divide)
    return calculation.get.result()