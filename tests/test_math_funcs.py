"""Math Funcs Tests

Unit tests for math_funcs module
"""
import utils.math_funcs as math_funcs

def test_square():
    """Tests math_funcs.square"""
    assert math_funcs.square(3) == 9

def test_cube():
    """Tests math_funcs.cube"""
    assert math_funcs.cube(2) == 8

def test_less():
    """Tests math_funcs.less"""
    assert math_funcs.less(2, 6) is True
    assert math_funcs.less(6, 2) is False

def test_greater():
    """Tests math_funcs.greater"""
    assert math_funcs.greater(6, 2) is True

def test_iseven():
    """Tests math_funcs.iseven"""
    assert math_funcs.iseven(3) is False
    assert math_funcs.iseven(26) is True

def test_add():
    """Tests math_funcs.add"""
    assert math_funcs.add(1, 2) == 3

def test_mult():
    """Tests math_funcs.mult"""
    assert math_funcs.mult(2, 3) == 6

def test_div():
    """Tests math_funcs.div"""
    assert math_funcs.div(6, 3) == 2
