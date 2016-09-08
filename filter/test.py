from bloom_spec import BloomSpec
k, M = BloomSpec.optimalFilterParams(0.01, 10000)
print(k,M)