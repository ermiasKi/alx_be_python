class Calculator:
    caculation_type =  "Arithmetic Operations"


    @classmethod
    def multiply(cls, a, b):
        print(cls.caculation_type)
        return a*b
    

    @staticmethod
    def add(a,b):
        return a + b
    