'''************ Base operation section for functions *************'''
class Calculation:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation  = operation
        

"""************* Allows operations between a & b *****************"""
def get_result(self):
        return self.operation(self.a, self.b)
