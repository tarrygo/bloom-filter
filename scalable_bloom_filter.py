from bloom_filter import BloomFilter
class ScalableBloomFilter():
	"""docstring for ScalableBloomFilter"""
	'SMALL_GROWTH' = 2
	'LARGE_GROWTH' = 4
	def __init__(self, expected_inserts, error_rate, mode='SMALL_GROWTH'):
		self.sbfilters = []

		sbfilter = BloomFilter(expected_inserts, error_rate)
		self.sbfilters.append(sbfilter)
		self.error_prob_ratio = 0.9
		self.space_scale = mode

	def add(self, key):
		bfilter = self.sbfilters[-1]
		if !bfilter.can_accomodate:
			new_expected_inserts = bfilter.expected_inserts * self.space_scale
			new_error_rate = bfilter.error_rate * self.error_prob_ratio
			new_bfilter = BloomFilter(new_expected_inserts, new_error_rate)
			sbfilters.append(new_bfilter)
			bfilter = sbfilters
		bfilter.add(key)

	def __contains__(self, key):
		for bfilter in reversed(self.sbfilters):
			if key in bfilter:
				return True
		return False

		