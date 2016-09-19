import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from filters.bloom_filter import BloomFilter
import unittest

class BloomFilterTest(unittest.TestCase):

	def setUp(self):
		self.capacity = 100
		self.error_rate = 0.01
		self.bfilter = BloomFilter(self.capacity, self.error_rate)

	def add_random(self, inserts):
		for i in range(inserts):
			self.bfilter.add(i)

	def test_bloom_params(self):
		bfilter = BloomFilter(1000, 0.01)
		self.assertEqual(bfilter.k, 7)
		self.assertEqual(bfilter.m, 1369)
		self.assertEqual(bfilter.M, 9586)

	def test_add(self):
		self.bfilter.add(200)
		self.assertTrue(200 in self.bfilter)

	def test_clear(self):
		self.add_random(100)
		self.bfilter.clear()
		self.assertEqual(self.bfilter.count, 0)


	def test_can_accomodate(self):
		self.add_random(99)
		self.assertTrue(self.bfilter.can_accomodate())
		self.bfilter.add(123)
		self.assertFalse(self.bfilter.can_accomodate())


if __name__ == '__main__':
    unittest.main()

