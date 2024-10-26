from decimal import Decimal
from typing import Callable


'''************ Base operation section for functions *************'''


class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]): #Type hints added for used parameters and return type
        self.a = a #Allows for first operand to be initialized
        self.b = b #Allows for second operand to be initialized
        self.operation  = operation #Allows function that matches signatures
        





    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(a , b, operation) #Return Calculation based on Argument provided





    def perform(self) -> Decimal:
        return self.operation(self.a, self.b)




    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"