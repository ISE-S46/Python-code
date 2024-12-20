from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Homework5_1").getOrCreate()
data = [("Alice", 20, 85, "Math"), ("Bob", 22, 78, "Science"), ("Charlie", 21, 90, "Math"), ("David", 23, 76, "History"), ("Eva", 20, 92, "Science")]
columns = ["Name", "Age", "Grade", "subject"]
df = spark.createDataFrame(data, columns)
df.show()

print("Records:",df.count())
print()

df.createOrReplaceTempView("list")
spark.sql("SELECT * FROM list WHERE Age >= 21").show()
spark.sql("SELECT AVG(Age) FROM list;").show()
spark.sql("SELECT * FROM list WHERE subject = 'Math';").show()
spark.stop()