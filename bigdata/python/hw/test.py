# Imports
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate() 

rdd2 = spark.sparkContext.textFile('/tmp/catbd125/Tekle/MapReduce/file.txt')
content_rdd = rdd2.map(lambda x: x[1])
words_rdd = content_rdd.flatMap(lambda line: line.split())
word_counts = words_rdd.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
for word, count in word_counts.collect():
    print "{0}: {1}".format(word, count)
