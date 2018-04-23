#####Section 9.4
import random

def float_random(low ,high):
	x = random.random()
	x = low + (high - low)*x
	return x
#Testcase
print float_random(1,10)
print float_random(2,4)
print float_random(3,5)
#####Secton 9.7
#List
t = [random.random() for i in range(1200)]
u = [random.random() for i in range(1600)]
#Code
numBuckets = 8 
buckets = [0] * numBuckets 
bucketWidth = 1.0 / numBuckets
def inBucket(t, low, high): 
  count = 0 
  for num in t: 
    if low < num < high: 
      count = count + 1 
  return count 
#Testcase 
#Test 1
for i in range(numBuckets): 
  low = i * bucketWidth 
  high = low + bucketWidth 
  buckets[i] = inBucket(t, low, high) 
print buckets
#Test 2 
for i in range(numBuckets): 
  low = i * bucketWidth 
  high = low + bucketWidth 
  buckets[i] = inBucket(u, low, high) 
print buckets
#####Section 9.8
def histogram(List, numBuckets):
	buckets = [0] * numBuckets 
	bucketWidth = 1.0 / numBuckets
	for i in range(numBuckets): 
  		low = i * bucketWidth 
  		high = low + bucketWidth 
  		buckets[i] = inBucket(List, low, high) 
	return buckets
#Testcase 
print histogram(t, 10)
print histogram(u, 4)	