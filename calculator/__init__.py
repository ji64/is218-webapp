""" This is the Calculator Class"""


class Calculator:
    """ This is the default result property"""
    result = 0

    def add(self, x):
        self.result += x
        return self.result

    def subtract(self, x):
        self.result -= x
        return self.result

    def multiply(self, x):
        self.result *= x
        return self.result

    def divide(self, x):
        self.result /= x
        return self.result
