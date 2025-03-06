import unittest
from coe_6710110245.Funny_String import funnyString

class TestFunnyString(unittest.TestCase):
    def test_example_funny(self):
        self.assertEqual(funnyString("acxz"), "Funny")
    
    def test_example_not_funny(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")
    
    def test_all_same_characters(self):
        self.assertEqual(funnyString("aaa"), "Funny")
    
    def test_two_characters(self):
        self.assertEqual(funnyString("ab"), "Funny")
    
    def test_edge_case(self):
        self.assertEqual(funnyString("az"), "Funny")
        self.assertEqual(funnyString("za"), "Funny")
    
    def test_single_character(self):
        self.assertEqual(funnyString("a"), "Funny")
    
    def test_all_same_characters(self):
        self.assertEqual(funnyString("zzzz"), "Funny")
    
    def test_non_sequential_characters(self):
        self.assertEqual(funnyString("abz"), "Not Funny")
    
    def test_large_input(self):
        self.assertEqual(funnyString("abcdefghijklmnopqrstuvwxyz"), "Funny")

if __name__ == '__main__':
    unittest.main()


