import unittest
import getInt as getInt

testInt = getInt.getInt("Integer",1,15)
print(testInt)

class TestgetInt(unittest.TestCase):
    def test_int_value() -> None:
        self.assertEqual(getInt.getInt("Test", 0, 0), 1)
    def test_string_value() -> None:
        self.assertEqual(getInt.getInt("Test", 0, 0), "Test")
    def test_float_value() -> None:
        self.assertEqual(getInt.getInt("Test", 0, 0), 1.0)
    def test_negative_value() -> None: pass