import unittest
import importlib
stairs = importlib.import_module('partitions-with-distinct-terms')

class TestCases(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(stairs.solution(100), 444792)
        self.assertEqual(stairs.solution(1), 0)
        self.assertEqual(stairs.solution(2), 0)
        self.assertEqual(stairs.solution(500), 732986521245023)
        
        
if __name__ == '__main__':
    unittest.main()
