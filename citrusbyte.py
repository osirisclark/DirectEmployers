"""
Write some code, that will flatten an array of arbitrarily nested arrays of
integers into a flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4]
"""

import re


def flatten(a):
    return re.findall(r'\d+', str(a))


print(flatten([[1,2,[3]],4]), "return: ['1', '2', '3', '4']")
