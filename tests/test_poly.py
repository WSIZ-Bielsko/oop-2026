import pytest
import math
from oop_2026.bible.basic.poly import Rectangle, Square, Circle, Triangle


def test_rectangle_area():
    """Test rectangle area calculation."""
    rec = Rectangle(4, 5)
    assert rec.get_area() == 20.0


def test_square_area():
    """Test square area calculation."""
    sq = Square(7)
    assert sq.get_area() == 49.0


def test_circle_area():
    """Test circle area calculation."""
    circle = Circle(3)
    expected = 9.0 * math.pi
    assert circle.get_area() == pytest.approx(expected)


def test_triangle_area_right_triangle():
    """Test triangle area with right triangle (3-4-5)."""
    tri = Triangle(3, 4, 5)
    assert tri.get_area() == pytest.approx(6.0)


def test_triangle_area_equilateral():
    """Test triangle area with equilateral triangle."""
    tri = Triangle(6, 6, 6)
    expected = (math.sqrt(3) / 4) * 36
    assert tri.get_area() == pytest.approx(expected)


@pytest.mark.parametrize("width,height,expected", [
    (2, 3, 6.0),
    (10, 5, 50.0),
    (1, 1, 1.0),
    (7.5, 4, 30.0)
])
def test_rectangle_parametrized(width, height, expected):
    """Test rectangle with multiple parameter sets."""
    rec = Rectangle(width, height)
    assert rec.get_area() == pytest.approx(expected)