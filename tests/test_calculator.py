from calculator import add, subtract, multiply, divide
'''Initial Calculator Test'''
from calculator import Calculator

'''This section checks that the addition works'''

def test_addition():
    assert Calculator.add(2,2) == 4
    
    '''Checks subtraction for calculator'''
def test_subtraction():
        assert Calculator.subtract(2,2) == 0
        
def test_multiplication():
        assert Calculator.multiply(5,5) == 25
        
def test_division():
        assert Calculator.divide(6,2)  == 3