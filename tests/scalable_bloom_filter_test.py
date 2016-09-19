import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from filters.scalable_bloom_filter import ScalableBloomFilter
import unittest

class ScalableBloomFilterTest(unittest.TestCase):

	def setUp(self):
		self.capacity = 10000
		self.error_rate = 0.01
		self.sbfilter = ScalableBloomFilter(self.capacity, self.error_rate)

	def add_random(self, start, end):
		for i in range(start, end):
			self.sbfilter.add(i)

	def test_add(self):
		self.sbfilter.add(200)
		self.assertTrue(200 in self.sbfilter)

	def test_over_capacity(self):
		self.add_random(0, 9999)
		self.assertEqual(len(self.sbfilter.sbfilters), 1)
		self.add_random(10000, 11000)
		self.assertEqual(len(self.sbfilter.sbfilters), 2)



if __name__ == '__main__':
    unittest.main()

