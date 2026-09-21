from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, upper, to_date

spark = SparkSession.builder.appName("CustomerSalesCleaning").getOrCreate()

input_base = "s3://customer-sales-data/raw/"
output_base = "s3://customer-sales-data/processed/"

customers = spark.read.option("header", True).csv(input_base + "customers/")
products = spark.read.option("header", True).csv(input_base + "products/")
orders = spark.read.option("header", True).csv(input_base + "orders/")
order_items = spark.read.option("header", True).csv(input_base + "order_items/")

customers = (
    customers.dropDuplicates(["customer_id"])
    .fillna({"city": "Unknown", "state": "Unknown"})
    .withColumn("city", upper(trim(col("city"))))
    .withColumn("registration_date", to_date("registration_date"))
)

products = (
    products.dropDuplicates(["product_id"])
    .withColumn("product_name", trim(col("product_name")))
    .withColumn("price", col("price").cast("double"))
)

orders = (
    orders.dropDuplicates(["order_id"])
    .withColumn("order_date", to_date("order_date"))
)

order_items = (
    order_items.dropDuplicates(["order_item_id"])
    .withColumn("quantity", col("quantity").cast("int"))
    .withColumn("unit_price", col("unit_price").cast("double"))
)

customers.write.mode("overwrite").parquet(output_base + "customers/")
products.write.mode("overwrite").parquet(output_base + "products/")
orders.write.mode("overwrite").parquet(output_base + "orders/")
order_items.write.mode("overwrite").parquet(output_base + "order_items/")

spark.stop()
