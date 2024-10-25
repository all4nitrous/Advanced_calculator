from calculator import add, subtract, multiply, divide
from calculator.calculation import Calculation

class Calculator:

    @staticmethod
    def add(a,b):
        calculation = Calculation(a, b, add)
        return calculation.get.result()


    @staticmethod
    def subtract(a,b):
        calculation = Calculation(a, b, subtract)
        return calculation.get.result()


    @staticmethod
    def multiply(a,b):
        calculation = Calculation(a, b, multiply)
        return calculation.get.result()
      

    @staticmethod
    def divide(a,b):
        calculation = Calculation(a, b, divide)
        return calculation.get.result()