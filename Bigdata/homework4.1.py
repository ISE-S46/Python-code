from pyspark import SparkContext
sc = SparkContext('local', 'Question_1')
rdd = sc.parallelize([1, 2, 3, 4, 5, 6], numSlices=2)
# sum of the squares of all even numbers.
filtered_rdd = rdd.filter(lambda x: x % 2 == 0)
mapped_rdd = filtered_rdd.map(lambda x: x ** 2)
result = mapped_rdd.reduce(lambda x, y: x + y)
print(result)
sc.stop()