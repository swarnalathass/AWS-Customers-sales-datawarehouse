# AWS Glue Setup

## Database
Create a Glue Data Catalog database:
`customer_sales_db`

## Crawlers
Create crawlers for the raw S3 paths:
- customers
- products
- orders
- order_items

Point each crawler at the corresponding S3 prefix and run it.

## ETL
Create an AWS Glue Spark job and adapt `pyspark/sales_pipeline.py`.
Configure:
- IAM role with S3 read/write and Glue permissions
- Glue version compatible with your PySpark code
- Temporary directory
- Output S3 location

After the ETL job completes, crawl the processed/analytics prefixes if
you want Athena tables automatically created.
