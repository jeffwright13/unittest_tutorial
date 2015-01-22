import unittest

class SimplisticTest(unittest.TestCase):
    def testTrue(self):
        self.assertTrue(True)
    def testFalse(self):
        self.assertFalse(False)
    def testFalse2(self):
        self.assertFalse(True)
        
if __name__ == "__main__":
    unittest.main()