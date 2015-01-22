import unittest

class SimplisticTest(unittest.TestCase):
    def testTrue(self):
        self.assertTrue(True)
    def testTrue2(self):
        self.assertTrue(False)
    def testFalse(self):
        self.assertFalse(False)
    def testFalse2(self):
        self.assertFalse(True)
    def testError(self):
        raise RuntimeError('Test error!')
        
if __name__ == "__main__":
    unittest.main()