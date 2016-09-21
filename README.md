# bloom-filter
A simple and easy to use python library implementing scalable bloom filters. It is based on the implementation as described in the following paper:
* http://gsd.di.uminho.pt/members/cbm/ps/dbloom.pdf

#Usage:
### Creating Bloom filter:
```
from filters.bloom_filter import BloomFilter
bfilter = BloomFilter(capacity, error_rate)
#capacity = no of expected insertions.
#error_rate: desired false positive error rate
```
### Add keys in filter:
```
bfilter.add(<key_name>)
bfilter.add('foo')
```

### Check if key is present in filter:
```
key in bfilter   #Overidden __contains__
# returns true(with expected false positive rate) or false
```

### Create Scalable bloom filter:
```
bfilter = ScalableBloomFilter(capacity, error_rate, mode)
#capacity = no of expected insertions.
#error_rate: desired false positive error rate
#mode: SMALL_GROWTH or HIGH_GROWTH
  #SMALL_GROWTH: If the set growth is expected to be in 2 orders of magnitude 
  #HIGH_GROWTH: If the set growth is expected to be in 6 orders of magnitude
```

#Benchmarks:
#### Time-Inserts: Time took to add x no. of keys
![time-capacity](https://cloud.githubusercontent.com/assets/12013472/18701266/6543df8e-7ff9-11e6-8d99-7f64dfded66c.png)





#### FalsePositiveRate-inserts: Experimental false positive rate as we increase the inserts way above the expected inserts.
Notice the false positive rate reaches 1 as we increase the inserts by 10x
![falsepostive_trials](https://cloud.githubusercontent.com/assets/12013472/18701274/6fde873c-7ff9-11e6-9c40-42cbd728735e.png)




####Scalable-FalsePositiveRate-inserts: Same as 2nd benchmark but with scalable bloom filter
![scalable_bf_small_growth](https://cloud.githubusercontent.com/assets/12013472/18701283/75f7d790-7ff9-11e6-9f5c-8ec176cac475.png)
