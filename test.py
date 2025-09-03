from typhe import *

class Calculator(struct):
    def __init__(self):
        super().__init__({
            "operator": char,
            "number1": uint32,
            "number2": uint32
        })

calculator = Calculator()

calculator.number1 = uint32(7)
calculator.number2 = uint32(10)
calculator.operator = char('*')