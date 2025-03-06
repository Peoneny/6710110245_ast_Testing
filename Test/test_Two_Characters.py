import unittest
from coe_6710110245.Two_Characters import alternate

class TestAlternateFunction(unittest.TestCase):
    def test_example(self):
        self.assertEqual(alternate("beabeefeab"), 5)
    
    def test_simple_alternating(self):
        self.assertEqual(alternate("aba"), 3) 
        self.assertEqual(alternate("ab"), 2) 
    
    def test_single_character(self):
        self.assertEqual(alternate("a"), 0)
    
    def test_all_same_characters(self):
        self.assertEqual(alternate("aaaa"), 0)
    
    def test_alternating_longer_string(self):
        self.assertEqual(alternate("cacacac"), 7)
    
    def test_no_valid_alternation(self):
        self.assertEqual(alternate("bbcbcc"), 0)

if __name__ == '__main__':
    unittest.main()