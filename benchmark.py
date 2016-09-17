from bloom_filter import BloomFilter
from scalable_bloom_filter import ScalableBloomFilter
import matplotlib.pyplot as plt
import sys, time

def main():
	error_rate = 0.01
	time_capacity_benchmark()
	false_positive_rate_benchmark(error_rate)
	false_positive_rate_benchmark_scalable(error_rate)

def time_capacity_benchmark():
	time_array =[]
	capacity_arr =[]
	for i in range(1000, 100000, 1000):
		time_taken = add_time(i, error_rate)
		time_array.append(time_taken)
		capacity_arr.append(i)
	plt.plot(capacity_arr, time_array, 'ro')
	plt.ylabel('Time')
	plt.xlabel('No. of insertions')
	plt.show()

def false_positive_rate_benchmark(error_rate):
	trial_arr = []
	fps_rate = []
	capacity = 10000
	bfilter = BloomFilter(capacity, error_rate)
	for trial in range(10000, 100000, 1000):
		fp = 0
		for i in range(trial):
			bfilter.add(i)
		for i in range(trial, 2*trial+1):
			if i in bfilter:
				fp+=1
		fp_rate = fp/float(trial)
		fps_rate.append(fp_rate)
		trial_arr.append(trial)
		
	plt.plot(trial_arr, fps_rate, 'bs')
	plt.ylabel('False Positive Rate')
	plt.xlabel('No of Trials')
	plt.show()

def false_positive_rate_benchmark_scalable(error_rate):
	trial_arr = []
	fps_rate = []
	capacity = 10000
	bfilter = ScalableBloomFilter(capacity, error_rate)
	for trial in range(10000, 100000, 1000):
		fp = 0
		for i in range(trial):
			bfilter.add(i)
		for i in range(trial, 2*trial+1):
			if i in bfilter:
				fp+=1
		fp_rate = fp/float(trial)
		fps_rate.append(fp_rate)
		trial_arr.append(trial)
		
	plt.plot(trial_arr, fps_rate, 'bs')
	plt.ylabel('False Positive Rate')
	plt.xlabel('No of Trials')
	plt.show()



def add_time(capacity, error_rate):
	bfilter = BloomFilter(capacity, error_rate)
	start_time = time.time()
	for i in range(capacity):
		bfilter.add(i)
	end_time = time.time()
	return end_time - start_time

if __name__ == '__main__':
	status = main()
	sys.exit(status)
