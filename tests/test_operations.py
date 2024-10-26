import pytest
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import divide

'''****************** Operations Testing *********************'''


def test_operation(a, b, operation, expected):
    calculation = Calculation.create(a, b, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"


'''************** Testing the divide by zero exception *****************'''


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculation = Calculation(Decimal('10'), Decimal('0'), divide) 
            calculation.perform()
            
def test_create_calculation():
    calc = Calculation.create(Decimal(1), Decimal(2), lambda a, b: a + b)
    assert isinstance(calc, Calculation)

def test_repr_calculation():
    calc = Calculation(Decimal(1), Decimal(2), lambda a, b: a + b)
    assert repr(calc) == "Calculation(1, 2, <lambda>)"






