import unittest
import importlib
colourings = importlib.import_module('non-equivalent-colourings')

class TestCases(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(colourings.solution(1,1,1),
                         1)
        self.assertEqual(colourings.solution(10,10,1),
                         1)
        self.assertEqual(colourings.solution(1,1,1000),
                         1000)
        self.assertEqual(colourings.solution(7,3,1000),
                         33068783763227519014651588965450182424626554362604265581000)
        self.assertEqual(colourings.solution(10,10,1000),
                         75940584281266233059295963476813407690465303634028067643120115987638768360299350432189628371332144284588102338919580926586742819469270026586348030871938085197343689280790904580324483625413736702601041419903161751121037817588203800360996035121655697677217564930154927270848934180754000000)
                         
if __name__ == '__main__':
    unittest.main()
