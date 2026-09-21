from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

spark = SparkSession.builder.appName("SalesTransformation").getOrCreate()

base = "s3://customer-sales-data/processed/"

orders = spark.read.parquet(base + "orders/")
items = spark.read.parquet(base + "order_items/")
products = spark.read.parquet(base + "products/")

completed_orders = orders.filter(col("order_status") == "Completed")

sales = (
    completed_orders
    .join(items, "order_id")
    .join(products.select("product_id", "product_name", "category"), "product_id")
    .withColumn("revenue", col("quantity") * col("unit_price"))
)

sales.write.mode("overwrite").partitionBy("category").parquet(
    "s3://customer-sales-data/analytics/sales/"
)

category_summary = (
    sales.groupBy("category")
    .agg(spark_sum("revenue").alias("total_revenue"))
)

category_summary.show()

spark.stop()
