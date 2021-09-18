# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(10,6,8),'Right','10,6,8 is a Right triangle')
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 should be equilateral')

    def testEquilateralTriangleC(self): 
        self.assertEqual(classifyTriangle(50,50,50),'Equilateral','50,50,50 should be equilateral')

    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(2,2,1),'Scalene','2,2,1 should be scalene')

    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(50,50,100),'Scalene','50,50,100 should be scalene')

    def testOutofBoundsTriangleA(self): 
        self.assertEqual(classifyTriangle(201,2,1),'InvalidInput')

    def testOutofBoundsTriangleB(self): 
        self.assertEqual(classifyTriangle(-1,2,1),'InvalidInput')

    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(10,1,12),'Isoceles','10,1,12 should be isoceles')

    def testIsocelesTriangleB(self): 
        self.assertEqual(classifyTriangle(8,4,10),'Isoceles','8,4,10 should be isoceles')
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

