import unittest

import srcFunctions

class TestClass(unittest.TestCase):

    def test_combiningStrings(self):

        string1 = "hello"
        string2 = "TCNJ"

        combinedString = srcFunctions.concatStrings(string1, string2)

        return self.assertEqual(combinedString, "hello TCNJ")

    def test_multiply(self):

        int1 = 10
        int2 = 20

        productOfTwoNums = srcFunctions.multiplyTwoNumbers(int1, int2)

        return self.assertEqual(productOfTwoNums, 200)

if __name__ == "__main__":
    unittest.main()