from calculator.calculation import Calculation
from typing import List

'''************* Calculations Section & stored History **************'''


class Calculations:
    history: List[Calculation] = []
   
   
    '''****************** Add results to history ************'''
    
    
    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)
        
        
    '''*************** Get History of results **************'''
    
    
    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history
    
    
    '''**************** Clear History *****************'''
    
    @classmethod 
    def clear_history(cls):
        cls.history.clear()
        
        
    '''**************** Retrieve Latest history **************** '''
    
    
    @classmethod
    def get_latest(cls) -> Calculation:
        if cls.history:                #If no History, returns None
            return cls.history[-1]
        return None
    
    
    '''*********** Return List of Calculations by name **************'''
    
    
    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]