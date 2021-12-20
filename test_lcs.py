import unittest
import lcs

class TestLcsMethods(unittest.TestCase):
    def test_lcs(self):
        self.assertEqual(4,lcs.lcs('myabcuuu','abcjju'))
        self.assertEqual(0,lcs.lcs('abcdef','ghijk'))



if __name__ == '__main__':
    unittest.main()