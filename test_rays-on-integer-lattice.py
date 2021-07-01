import unittest
import importlib
rays = importlib.import_module('rays-on-integer-lattice')

class TestCases(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(rays.solution([300,275], [150,150], [185,100], 500), 9)
        self.assertEqual(rays.solution([200,200], [1,1], [2,2], 1000), 79)
        self.assertEqual(rays.solution([500,500], [1,1], [100,75], 1000), 12)
        self.assertEqual(rays.solution([5,5], [1,1], [2,3], 1000), 113727)
        self.assertEqual(rays.solution([4,10], [3,1], [2,7], 500), 19157)
        
        
if __name__ == '__main__':
    unittest.main()
