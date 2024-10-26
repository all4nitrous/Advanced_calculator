from calculator.operations import add, subtract, multiply, divide


'''This section checks that the addition works'''

def test_addition():
    assert add(2,2) == 4
    
    '''Checks subtraction for calculator'''
def test_subtraction():
        assert subtract(2,2) == 0
        
def test_multiply():
        assert multiply(5,5) == 25
        
def test_divide():
        assert divide(6,2)  == 3