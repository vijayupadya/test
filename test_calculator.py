"""
Unit tests for the calculator module.
"""
import pytest
from calculator import add, subtract, multiply, divide, power


class TestAddition:
    """Tests for the add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2, -3) == -5
        assert add(-10, -20) == -30
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(5, -3) == 2
        assert add(-5, 3) == -2
    
    def test_add_zero(self):
        """Test adding zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        assert add(2.5, 3.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)


class TestSubtraction:
    """Tests for the subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(20, 10) == 10
    
    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        assert subtract(-5, -3) == -2
        assert subtract(-10, -20) == 10
    
    def test_subtract_mixed_numbers(self):
        """Test subtracting positive and negative numbers."""
        assert subtract(5, -3) == 8
        assert subtract(-5, 3) == -8
    
    def test_subtract_zero(self):
        """Test subtracting zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0


class TestMultiplication:
    """Tests for the multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(10, 5) == 50
    
    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        assert multiply(-2, -3) == 6
        assert multiply(-10, -5) == 50
    
    def test_multiply_mixed_numbers(self):
        """Test multiplying positive and negative numbers."""
        assert multiply(5, -3) == -15
        assert multiply(-5, 3) == -15
    
    def test_multiply_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(0, 0) == 0
    
    def test_multiply_one(self):
        """Test multiplying by one."""
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5


class TestDivision:
    """Tests for the divide function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide(6, 3) == 2
        assert divide(10, 5) == 2
    
    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        assert divide(-6, -3) == 2
        assert divide(-10, -5) == 2
    
    def test_divide_mixed_numbers(self):
        """Test dividing positive and negative numbers."""
        assert divide(6, -3) == -2
        assert divide(-6, 3) == -2
    
    def test_divide_zero_numerator(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0
        assert divide(0, -5) == 0
    
    def test_divide_by_zero(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
    
    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        assert divide(7, 2) == 3.5
        assert divide(1, 3) == pytest.approx(0.3333333, rel=1e-6)


class TestPower:
    """Tests for the power function."""
    
    def test_power_positive_exponent(self):
        """Test raising to a positive exponent."""
        assert power(2, 3) == 8
        assert power(5, 2) == 25
    
    def test_power_zero_exponent(self):
        """Test raising to the power of zero."""
        assert power(5, 0) == 1
        assert power(100, 0) == 1
    
    def test_power_one_exponent(self):
        """Test raising to the power of one."""
        assert power(5, 1) == 5
        assert power(100, 1) == 100
    
    def test_power_negative_exponent(self):
        """Test raising to a negative exponent."""
        assert power(2, -1) == 0.5
        assert power(10, -2) == 0.01
    
    def test_power_fractional_exponent(self):
        """Test raising to a fractional exponent."""
        assert power(4, 0.5) == 2.0
        assert power(27, 1/3) == pytest.approx(3.0)
