from calculator.calculation import Calculation
from typing import Callable, List
from decimal import Decimal

'''************* Calculations Section & stored History **************'''


class Calculations:
    history: List[Calculation] = []
   
   
    '''****************** Add results to history ***************S'''
    
    
    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)
        
        
    '''*************** Get History of results **************'''
    
    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history
    
    
    '''********************** Clear History *******************'''
    
    
    def clear_history(cls):
        cls.history.clear()
        
        
    '''**************** Retrieve Latest history **************** '''
    
    
    def get_latest(cls) -> Calculation:
        if cls.history:                #If no History, returns None
            return cls.history[-1]
        return None