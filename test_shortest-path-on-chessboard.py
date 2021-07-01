import unittest
import importlib
knights = importlib.import_module('shortest-path-on-chessboard')

class TestCases(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(knights.solution([10,10],(0,0),(1,1)), 4)
        self.assertEqual(knights.solution([10,10],(0,0),(2,2)), 4)
        self.assertEqual(knights.solution([10,10],(1,1),(2,2)), 2)
        self.assertEqual(knights.solution([4,4],(3,3),(3,3)), 0)
        self.assertEqual(knights.solution([10000,50000],(1832,8372),(210,4202)), 2086)
             
if __name__ == '__main__':
    unittest.main()
