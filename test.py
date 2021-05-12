import unittest
from Basic import Cross_Line
from random import random


class NameTestCase(unittest.TestCase):

    def test_findIntersection(self):
        ''' test a positive numbers, negative numbers, parallel lines'''
        self.assertEqual(Cross_Line.findIntersection(([[1,2],[3,4]],[[0,6],[7,8]])),(7.0, 8.0))
        self.assertEqual(Cross_Line.findIntersection(([[1,1],[2,2]],[[2,1],[3,2]])),None)
        self.assertEqual(Cross_Line.findIntersection(([[-1,2],[3,-4]],[[0,-6],[-7,8]])),(-13.0, 20.0))

    def test_findIntersection_Error(self):
        self.assertRaises(IndexError,Cross_Line.findIntersection,([[-1,2],[3,-4]],[[0,-6]]))
        self.assertRaises(TypeError,Cross_Line.findIntersection,([[-1,2],[3,-4]],[[0,-6],['a',2]]))






if __name__ == '__main__':
    unittest.main()
