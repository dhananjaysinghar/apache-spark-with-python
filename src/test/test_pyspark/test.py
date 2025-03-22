from pyspark.sql import SparkSession
from pymongo import MongoClient
import math

# Constants
MONGO_URI = "mongodb://test:password@localhost:27017/order-handling.bookings?authSource=admin"
DATABASE_NAME = "order-handling"
COLLECTION_NAME = "bookings"
PARTITION_SIZE = 50  # Number of records per partition
PARQUET_PATH = "/Users/dhananjayasamantasinghar/.ivy2/data/bookings_partitioned"
# /Users/dhananjayasamantasinghar/.ivy2/jars

def get_total_record_count():
    try:
        with MongoClient(MONGO_URI) as client:
            stats = client[DATABASE_NAME].command("collStats", COLLECTION_NAME)
            return stats.get("count", 0)
    except Exception as e:
        print(f"Error fetching record count: {e}")
        return 0


def read_mongo_with_partitioning():
    total_records = get_total_record_count()
    if total_records == 0:
        print("No records found in the collection. Exiting.")
        return

    num_partitions = max(1, math.ceil(total_records / PARTITION_SIZE))
    print(f"Total records: {total_records}, Computed partitions: {num_partitions}")

    spark = SparkSession.builder \
        .appName("MongoDB Partitioned Read") \
        .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.2") \
        .config("spark.mongodb.input.uri", MONGO_URI) \
        .config("spark.mongodb.input.database", DATABASE_NAME) \
        .config("spark.mongodb.input.collection", COLLECTION_NAME) \
        .master("local[*]") \
        .getOrCreate()

    df = spark.read \
        .format("mongo") \
        .option("partitioner", "MongoPaginateByCountPartitioner") \
        .option("partitionKey", "_id") \
        .option("partitionSize", str(PARTITION_SIZE)) \
        .load()

    df = df.repartition(num_partitions)

    df.explain(True)

    # Partition statistics
    partition_sizes = df.rdd.glom().map(len).collect()
    print(f"Number of partitions after repartition: {len(partition_sizes)}")

    for i, size in enumerate(partition_sizes):
        print(f"Partition {i}: {size} records")

    # Show sample data
    df.show(10)

    # Compute final record count (to verify partitioning)
    print(f"Total records in DataFrame: {df.count()}")

    df.write.mode("overwrite").parquet(PARQUET_PATH)
    print(f"Partitioned Parquet files saved at: {PARQUET_PATH}")


    spark.stop()


if __name__ == "__main__":
    read_mongo_with_partitioning()
