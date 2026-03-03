from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import time

spark = SparkSession.builder.getOrCreate()

spark.sql("USE CATALOG workspace")
spark.sql("USE SCHEMA crime_data")

crime_df = spark.table("crime_parquet_table")

def test_partitions(num_partitions):
    spark.conf.set("spark.sql.shuffle.partitions", num_partitions)
    start = time.time()
    crime_df.groupBy("District").count().collect()
    end = time.time()
    print(f"{num_partitions} partitions: {end - start} seconds")

if __name__ == "__main__":
    test_partitions(200)
    test_partitions(400)
    test_partitions(800)
