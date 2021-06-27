import unittest
import importlib
probabilities = importlib.import_module('absorption-probabilities')

class TestCases(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(probabilities.solution(
                                                [[0]]
                                                ),
                                                 [1,1])
        self.assertEqual(probabilities.solution(
                                                [[0,0],
                                                 [0,0]]
                                                ),
                                                 [1,0,1])
        self.assertEqual(probabilities.solution(
                                                [[1,1],
                                                 [0,0]]
                                                ),
                                                 [1,1])
        self.assertEqual(probabilities.solution(
                                                [[0, 1, 0, 0, 0, 1],
                                                 [4, 0, 0, 3, 2, 0],
                                                 [0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0],
                                                 [0, 0, 0, 0, 0, 0]]
                                                ),
                                                 [0, 3, 2, 9, 14])
        
if __name__ == '__main__':
    unittest.main()
