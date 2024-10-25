from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

'''************** Pytest Fixture *************'''


@pytest.fixture
def setup_calculations():
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))


'''************************* Add Calculation to History **************************'''


def test_add_calculation(setup_calculations):
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc) #Adds calculation to History
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"


"""************************** Retrieve History ************************************"""


def test_get_history(setup_calculations):
    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"


'''******************* Clear Calculation History Test ************************'''


def test_clear_history(setup_calculations):
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"


'''******************* Tests Retrieval of Latest Calculations ************************'''


def test_get_latest(setup_calculations):
    """Test getting the latest calculation from the history."""
    latest = Calculations.get_latest()
    assert latest.a == Decimal('20') and latest.b == Decimal('3'), "Did not get the correct latest calculation"


'''******************* Find Operation Test ************************'''


def test_find_by_operation(setup_calculations):
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Did not find the correct number of calculations with subtract operation"
    
    
'''******************** Test for Empty History ************************'''    


def test_get_latest_with_empty_history():
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"