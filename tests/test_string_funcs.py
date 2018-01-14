"""String Funcs Tests

Unit tests for string_funcs module
"""
import utils.string_funcs as string_funcs

def test_strip_chars():
    """Tests string_funcs.strip_chars"""
    assert string_funcs.strip_chars('ABC') == 'abc'
    assert string_funcs.strip_chars('$-ABC?!!!') == 'abc'
