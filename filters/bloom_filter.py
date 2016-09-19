from bitarray import bitarray
from bloom_spec import BloomSpec
import mmh3

class BloomFilter():
	"""Create bllom filter for given false positive rate and no. of elements to be inserted.
	params: 
	error_rate
	expected_inserts

	class variable:
		k = no. of hashes, no of slices
		m = size of each slice

	"""
	def __init__(self, expected_inserts, error_rate):
		self.error_rate = error_rate
		self.expected_inserts = expected_inserts
		bloom_specs = BloomSpec.optimalFilterParams(error_rate, expected_inserts)
		self.k = bloom_specs['hash_count']
		self.m = bloom_specs['slice_size']
		self.M = bloom_specs['filter_size']
		bfilter = bitarray(self.M)
		bfilter.setall(False)
		self.bfilter = bfilter
		self.count = 0

	def add(self, key):
		calculated_hash = self._calculate_hash(key)
		offset = 0
		is_new_key = False
		for hashed_key in calculated_hash:
			key_pos = hashed_key + offset
			if (self.bfilter[key_pos] == 0):
				self.bfilter[key_pos] = 1
				is_new_key = True
			offset = offset + self.m
		if is_new_key:
			self.count +=1

	def __contains__(self, key):
		calculated_hash = self._calculate_hash(key)
		offset = 0
		for key in calculated_hash:
			key_pos = key + offset
			if self.bfilter[key_pos] == 0 :
				return False
			offset = offset + self.m
		return True

	def clear(self):
		self.bfilter.setall(False)
		self.count = 0

	def _calculate_hash(self, key):
		encoded_key = str(key).encode('utf8')
		results = []
		no_of_hashes = self.k 
		slice_size = self.m 
		hash1 = mmh3.hash(encoded_key)
		hash2 = mmh3.hash(encoded_key, hash1)
		#print('key: '+ str(key) + ' hash1: ' + str(hash1))
		for i in range(no_of_hashes):
			index = (hash1 + i*hash2)%slice_size
			#print('index is: '+ str(index))
			results.append(index)
		return results

	def can_accomodate(self):
		if self.count < self.expected_inserts:
			return True
		else: 
			return False

