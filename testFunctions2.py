import Functions2
import unittest

class TestFunctions2(unittest.TestCase):
    def test_isPali(self):
        self.assertEqual(Functions2.isPali("racecar"), "It is a palindrome.")
        self.assertEqual(Functions2.isPali("machine"), "It is not a palindrome.")

    def test_longword(self):
        self.assertEqual(Functions2.longword("qweasdzxcqweasdzxc asd ff asdas")[0], "qweasdzxcqweasdzxc")
        self.assertEqual(Functions2.longword("qweasdzxcqweasdzxc asd ff asdas")[1], 18)

    def test_isAnagram(self):
        self.assertEqual(Functions2.isAnagram("Wikipedia", "Extraordinary"), "These words ARE NOT anagrams of each other as they do not have the same number of letters in them.")
        self.assertEqual(Functions2.isAnagram("Apple", "Phone"), "These words ARE NOT anagrams of each other.")
        self.assertEqual(Functions2.isAnagram("Anagram", "Gramana"), "These words ARE anagrams of each other.")

    def test_SumofN(self):
        self.assertEqual(Functions2.SumofN(45, 120), ("The result of the sum is   165"))
        self.assertEqual(Functions2.SumofN(-33, 0), ("The result of the sum is   -33"))
        self.assertEqual(Functions2.SumofN(-15, -10), ("The result of the sum is   -25"))

    def test_NMA(self):
        self.assertEqual(Functions2.NMA(23, 10, 42, 72), ("Sum of the list of numbers is 147 and the average is 36.75."))
        self.assertEqual(Functions2.NMA(-31, 20, 6, 9), ("Sum of the list of numbers is 4 and the average is 1.0."))

if __name__ == '__main__':
    unittest.main()