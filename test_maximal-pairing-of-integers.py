import unittest
import importlib
pairings = importlib.import_module('maximal-pairing-of-integers')

class TestCases(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(pairings.solution([]),0)
        self.assertEqual(pairings.solution([1]),1)
        self.assertEqual(pairings.solution([2 for _ in range(999)]),999)
        self.assertEqual(pairings.solution([k for k in range(1,999)]),0)
        self.assertEqual(pairings.solution([2**k-1 for k in range(1,999)]),2)
                         
if __name__ == '__main__':
    unittest.main()
