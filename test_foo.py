#!/usr/bin/python

import unittest

class FooTest(unittest.TestCase):
    '''Sample test case -- FooTest()'''
    
    def setUp(self):
        '''Set up for testing...'''
        print 'FooTest: setUp()'
        
    def testA(self):
        '''Test routine A...'''
        print 'FooTest: testA'
        
    def testB(self):
        '''Test routine B...'''
        print 'FooTest: testB'
        
    def tearDown(sefl):
        '''Tear down from testing...'''
        print 'FooTest: tearDown()'
        
if __name__ == '__main__':
    unittest.main()