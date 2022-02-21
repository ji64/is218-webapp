"""Testing the Calculator"""
import pytest
from calculator import Calculator


def test_calculator_is_instance():
    # instantiating the Calculator Class
    calculator = Calculator()
    assert isinstance(calculator, Calculator)


def test_calculator_result_property():
    # instantiating the Calculator Class
    calc1 = Calculator()
    calc2 = Calculator()
    calc1.result = 5
    calc2.result = 6
    assert calc1.result == 5
    assert calc2.result == 6


def test_calculator_add_method():
    # instantiating the Calculator Class
    calculator = Calculator()
    assert calculator.add(1) == 1


def test_calculator_subtract_method():
    # instantiating the Calculator Class
    calculator = Calculator()
    assert calculator.subtract(1) == -1


def test_calculator_multiply_method():
    # instantiating the Calculator Class
    calculator = Calculator()
    calculator.result = 2
    assert calculator.multiply(3) == 6


def test_calculator_divide_method():
    # instantiating the Calculator Class
    calculator = Calculator()
    calculator.result = 2
    assert calculator.divide(2) == 1
