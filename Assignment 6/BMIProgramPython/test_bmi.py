import pytest
from BMIProgramPython import calculate_bmi, bmi_category

def test_normal_bmi():
    bmi = calculate_bmi(150, 5, 6)
    # Expected BMI ≈ 24.2
    assert round(bmi, 1) == 24.2

def test_weight_zero():
    with pytest.raises(ValueError):
        calculate_bmi(0, 5, 6)

def test_inches_too_high():
    with pytest.raises(ValueError):
        calculate_bmi(150, 5, 12)

def test_negative_feet():
    with pytest.raises(ValueError):
        calculate_bmi(150, -1, 5)

def test_non_numeric_weight():
    with pytest.raises(TypeError):
        calculate_bmi("abc", 5, 6)

def test_underweight_category():
    assert bmi_category(18.4) == "Underweight"

def test_normal_category():
    assert bmi_category(22) == "Normal weight"

def test_overweight_category():
    assert bmi_category(27) == "Overweight"

def test_bmi_not_numeric():
    with pytest.raises(TypeError):
        bmi_category("hello")

def test_bmi_zero_or_negative():
    with pytest.raises(ValueError):
        bmi_category(0)