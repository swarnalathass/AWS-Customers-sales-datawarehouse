# Entry-point example for an AWS Glue PySpark job.
# In AWS Glue Studio, adapt the S3 paths and Glue DynamicFrame APIs
# to your account configuration.

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

spark = SparkSession.builder.appName("CustomerSalesPipeline").getOrCreate()

RAW = "s3://customer-sales-data/raw/"
PROCESSED = "s3://customer-sales-data/processed/"
ANALYTICS = "s3://customer-sales-data/analytics/"

customers = spark.read.option("header", True).csv(RAW + "customers/")
products = spark.read.option("header", True).csv(RAW + "products/")
orders = spark.read.option("header", True).csv(RAW + "orders/")
items = spark.read.option("header", True).csv(RAW + "order_items/")

orders = orders.filter(col("order_status") == "Completed")
items = items.withColumn("quantity", col("quantity").cast("int"))                  .withColumn("unit_price", col("unit_price").cast("double"))

sales = (
    orders.join(items, "order_id")
          .join(products, "product_id")
          .withColumn("revenue", col("quantity") * col("unit_price"))
)

sales.write.mode("overwrite").parquet(ANALYTICS + "sales/")

sales.groupBy("category").agg(
    spark_sum("revenue").alias("total_revenue")
).show()

spark.stop()
