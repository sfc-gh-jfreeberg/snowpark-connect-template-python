from snowflake.snowpark_connect import init_spark_session
from pyspark.sql.functions import col, lit, upper, concat

# Create Spark session
print("Initializing Spark session...")
spark = init_spark_session()  # use connection_parameters={'connection_name': 'my_connection_name'} if you have a named connection in your config file

data = [
    (1, "alice", "engineering", 95000),
    (2, "bob", "marketing", 72000),
    (3, "carol", "engineering", 105000),
    (4, "david", "sales", 68000),
    (5, "eva", "engineering", 88000),
]
df = spark.createDataFrame(data, ["id", "name", "department", "salary"])

df_with_bonus = df.withColumn("bonus", col("salary") * 0.1)
df_with_bonus.show()

# Filter and transform
engineers = df.filter(col("department") == "engineering") \
    .withColumn("name_upper", upper(col("name"))) \
    .withColumn("greeting", concat(lit("Hello, "), col("name")))
engineers.show()

# Aggregate
df.groupBy("department").avg("salary").show()

# Stop the Spark session
spark.stop()
