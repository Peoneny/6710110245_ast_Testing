import unittest
from coe_6710110245.Grid_Challenge import gridChallenge

class TestGridChallenge(unittest.TestCase):
    def test_example(self):
        grid = [
            "ebacd",
            "fghij",
            "olmkn",
            "trpqs",
            "xywuv"
        ]
        self.assertEqual(gridChallenge(grid), "YES")
    
    def test_no_case(self):
        grid = [
            "zyx",
            "wvu"
        ]
        self.assertEqual(gridChallenge(grid), "NO")
    
    def test_single_row(self):
        grid = ["abc"]
        self.assertEqual(gridChallenge(grid), "YES")
    
    def test_single_column(self):
        grid = [
            "a",
            "b",
            "c"
        ]
        self.assertEqual(gridChallenge(grid), "YES")
    
    def test_all_same_characters(self):
        grid = [
            "aaa",
            "aaa",
            "aaa"
        ]
        self.assertEqual(gridChallenge(grid), "YES")

if __name__ == '__main__':
    unittest.main()