from pyspark import SparkContext
sc = SparkContext('local', 'Question_3')
rdd = sc.parallelize([10, 20, 15, 30, 50, 35, 40, 45, 25], numSlices=2)
EvenRdd = rdd.filter(lambda x: x % 2 == 0).collect()
print("a, ",EvenRdd)

MultipliedRdd = rdd.map(lambda x: x * 2).collect()
print("b, ",MultipliedRdd)

result = rdd.groupBy(lambda x: x <= 25).collect()
sorted_result = sorted([(x, sorted(y)) for (x, y) in result])
print("c i, ",sorted_result[1])
print("c ii, ",sorted_result[0])

grouped_rdd = rdd.groupBy(lambda x: "≤" if x <= 25 else ">")
result = grouped_rdd.mapValues(list).collect()
for group, values in result:
    print(f"{group}: {values}")
sc.stop()