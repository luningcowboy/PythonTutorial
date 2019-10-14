import unittest

from fk_math import *

class TestFKMath(unittest.TestCase):
    def test_one_equation(self):
        self.assertEqual(one_equation(5, 9), -1.8)
