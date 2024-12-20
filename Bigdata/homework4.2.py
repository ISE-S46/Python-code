from pyspark import SparkContext
sc = SparkContext('local', 'Question_2')
rdd = sc.parallelize([7, 2, 10, 5, 8, 3], numSlices=2)
max_even = rdd.filter(lambda x: x % 2 == 0).max()
print(max_even)
sc.stop()