import unittest
import multiply

class test_multiply(unittest.TestCase):
	def setUp(self):
		pass
		
	def test_two_pos(self):
		self.assertEqual(multiply.multiply(3, 6), 18)
	def test_two_neg(self):
		self.assertEqual(multiply.multiply(-1, -6), 6)
	def test_one_each(self):
		self.assertEqual(multiply.multiply(-5.5, 2), -11.0)
		
	def tearDown(sefl):
		pass
		
if __name__ == '__main__':
	unittest.main()