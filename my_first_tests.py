import pytest
from apps.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multyply_calculat_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multyply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculat_correctly(self):
        assert self.calc.division(self, 6, 2) == 3

    def test_division_calculate_failed(self):
        assert self.calc.division(self, 6, 2) == 2

    def test_subtraction_calculat_correctly(self):
        assert self.calc.subtraction(self, 7, 2) == 5

    def test_subtraction_calculate_failed(self):
        assert self.calc.subtraction(self, 7, 2) == 3

    def test_adding_calculat_correctly(self):
        assert self.calc.adding(self, 5, 7) == 12

    def test_adding_calculate_failed(self):
        assert self.calc.adding(self, 5, 7) == 10