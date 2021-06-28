import unittest

class TestClass(unittest.TestCase):

    def test_combiningStrings(self):

        string1 = "hello"
        string2 = "TCNJ"

        combinedString = string1 + " " + string2

        return self.assertEqual(combinedString, "hello TCNJ")

    def test_multiply(self):

        int1 = 10
        int2 = 20

        productOfTwoNums = int1 * int2

        return self.assertEqual(productOfTwoNumbers, 200)

if __name__ = "__main__":
    unittest.main()