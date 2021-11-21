import pytest


@pytest.mark.smoke
def test_mul__positive_int_values(calculator):
    assert calculator.mul(2, 3) == 6


@pytest.mark.smoke
def test_mul__negative_int_values(calculator):
    assert calculator.mul(-2, -3) == 6  


@pytest.mark.regression
def test_mul__mixed_int_values(calculator):
    assert calculator.mul(-2, 3) == -6


@pytest.mark.smoke
def test_mul__positive_float_values(calculator):
    assert calculator.mul(2.5, 3) == 7.5


@pytest.mark.smoke
def test_mul__negative_float_values(calculator):
    assert calculator.mul(-2.5, -3) == 7.5


@pytest.mark.regression
def test_mul__mixed_float_values(calculator):
    assert calculator.mul(2.5, -3) == -7.5
