"""String Funcs

String utility functions to be used for function compositon
"""

def strip_chars(str_val):
    """Removes special chars and lowercases a string"""
    return str_val.lower().rstrip(",.!)-*_?:;$'-\"").lstrip("-*'\"(_$'")
