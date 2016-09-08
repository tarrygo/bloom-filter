import math

class BloomSpec():
	"""This contains all the equations needed to calculate the specification of bloom filter."""
	
	@staticmethod
	def optimalFilterParams(error_rate, capacity):
		BloomSpec._validate(error_rate, capacity)
		k = BloomSpec.getOptimalNoOfHashes(error_rate)
		M = BloomSpec.getOptimalSizeOfFilter(error_rate, capacity)
		m = BloomSpec.getSliceSize(M, k)
		return {'hash_count':k, 'filter_size': M, 'slice_size': m}

	@staticmethod
	def getOptimalNoOfHashes(error_rate):
		return int(math.ceil(math.log((1/error_rate), 2)))

	@staticmethod
	def getOptimalSizeOfFilter(error_rate, capacity):
		numer = abs(capacity*(math.log(error_rate)))
		denom = 0.480453
		filter_size = int(math.ceil(numer/denom))
		return filter_size

	@staticmethod
	def getSliceSize(filter_size, no_of_hashes):
		return int(math.ceil(filter_size/no_of_hashes))

	@staticmethod
	def _validate(error_rate, capacity):
		if error_rate <= 0:
			raise "ERROR_RATE_SHOULD_BE_POSITIVE"
		elif capacity <= 1:
			raise "CAPCITY_SHOULD_BE_POSITIVE"
		else:
			return True



		