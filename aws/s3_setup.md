# Amazon S3 Setup

1. Create an S3 bucket, for example `customer-sales-data-<unique-id>`.
2. Create:
   - raw/customers/
   - raw/products/
   - raw/orders/
   - raw/order_items/
   - processed/
   - analytics/
3. Upload the CSV files from the `data/` folder into the matching raw paths.
4. Update the bucket name in the PySpark scripts before running them.
5. For production, enable versioning and configure least-privilege IAM policies.
