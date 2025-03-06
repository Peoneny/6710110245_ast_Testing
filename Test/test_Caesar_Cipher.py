import unittest
from coe_6710110245.Caesar_Cipher import caesarCipher

class TestCaesarCipher(unittest.TestCase):
    def test_sample_case(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")

    def test_all_lower(self):
        self.assertEqual(caesarCipher("abc", 3), "def")

    def test_all_upper(self):
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")

    def test_mixed_characters(self):
        self.assertEqual(caesarCipher("Hello-World!", 5), "Mjqqt-Btwqi!")

    def test_no_shift(self):
        self.assertEqual(caesarCipher("Hello-World!", 0), "Hello-World!")

    def test_large_shift(self):
        self.assertEqual(caesarCipher("Hello-World!", 52), "Hello-World!")
        self.assertEqual(caesarCipher("abc", 27), "bcd")

if __name__ == '__main__':
    unittest.main()