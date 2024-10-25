from calculator import add, subtract, multiply, divide
'''Initial Calculator Test'''
from calculator import add

'''This section checks that the addition works'''

def test_addition():
    assert add(2,2) == 4
    
    '''Checks subtraction for calculator'''
def test_subtraction():
        assert subtract(2,2) == 0
        
def test_multiplication():
        assert multiply(5,5) == 25
        
def test_division():
        assert divide(6,2)  == 3