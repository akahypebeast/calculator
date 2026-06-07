"""Unit tests for calculator logic."""

import pytest

from calculator.logic import add, subtract, multiply, divide


class TestAdd:
    """Tests for the add function."""

    def test_add_positive(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5

    def test_add_negative(self):
        """Test adding two negative numbers."""
        assert add(-1, -1) == -2

    def test_add_floats(self):
        """Test adding floats."""
        assert add(1.5, 2.5) == 4.0

    def test_add_zero(self):
        """Test adding zero."""
        assert add(0, 5) == 5


class TestSubtract:
    """Tests for the subtract function."""

    def test_subtract_positive(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2

    def test_subtract_negative_result(self):
        """Test subtraction yielding a negative result."""
        assert subtract(1, 5) == -4

    def test_subtract_floats(self):
        """Test subtracting floats."""
        assert subtract(3.5, 1.5) == 2.0


class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive(self):
        """Test multiplying positive numbers."""
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0

    def test_multiply_negative(self):
        """Test multiplying with a negative number."""
        assert multiply(-2, 3) == -6


class TestDivide:
    """Tests for the divide function."""

    def test_divide_positive(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5.0

    def test_divide_float_result(self):
        """Test division resulting in a float."""
        assert divide(1, 3) == pytest.approx(0.3333, rel=1e-3)

    def test_divide_by_zero_raises(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_negative(self):
        """Test dividing with a negative number."""
        assert divide(-6, 2) == -3.0
