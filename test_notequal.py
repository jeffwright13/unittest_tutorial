import unittest

class InequalityTest(unittest.TestCase):
    def testEqual(self):
        self.assertEqual(1, 5-4)
    def testNotEqual(self):
        self.assertNotEqual(0, 0.1)
    def testEqual2(self):
        self.assertEqual(-1, 5-4)
    def testNotEqual2(self):
        self.assertNotEqual(0, 100-100)

if __name__ == '__main__':
    unittest.main()