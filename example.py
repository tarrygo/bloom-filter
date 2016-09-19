from filters.bloom_filter import BloomFilter
from filters.scalable_bloom_filter import ScalableBloomFilter
capacity = 100
error_rate = 0.01
bfilter = BloomFilter(capacity, error_rate)


for i in range(capacity):
	bfilter.add(i)
print 4 in bfilter
print 200 in bfilter


print "--------------------"

sbfilter = ScalableBloomFilter(1000, 0.01)
for i in range(1000):
	sbfilter.add(i)
print 4 in sbfilter
print 1002 in sbfilter

for i in range(1000, 10000):
	sbfilter.add(i)
print len(sbfilter.sbfilters)

print 10005 in sbfilter
