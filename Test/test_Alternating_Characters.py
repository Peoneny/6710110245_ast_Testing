import unittest
from coe_6710110245.Alternating_Characters import alternatingCharacters

class TestAlternatingCharacters(unittest.TestCase):
    def test_all_same_characters(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
    
    def test_all_same_characters_2(self):
        self.assertEqual(alternatingCharacters("BBBBB"), 4)
    
    def test_alternating_string(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
    
    def test_alternating_string_2(self):
        self.assertEqual(alternatingCharacters("BABABA"), 0)
    
    def test_mixed_string(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)
    
    def test_empty_string(self):
        self.assertEqual(alternatingCharacters(""), 0)
    
    def test_single_character(self):
        self.assertEqual(alternatingCharacters("A"), 0)

if __name__ == '__main__':
    unittest.main()