####classes####

class Calculator:
    def __init__(self, number1, number2):
        self.number1 = int(number1)
        self.number2 = int(number2)

    def add(self):
        return self.number1 + self.number2
    
    def multiply(self):
        return self.number1 * self.number2
    

try:
    calc = Calculator(3, 5)
    print("Addition:", calc.add())
    print("Multiplication:", calc.multiply())
except ValueError:
    print("Please provide valid format.")

    
    
    

