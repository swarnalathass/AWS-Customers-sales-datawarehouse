# Amazon Redshift Setup

1. Create a Redshift Serverless workgroup or provisioned cluster.
2. Create a database/schema for the warehouse.
3. Run `sql/create_tables.sql`.
4. Load dimension tables from your curated S3 data.
5. Load `fact_sales` from the processed/analytics S3 output.
6. Run the queries in `sql/analytics_queries.sql`.

For a real deployment, use IAM roles for Redshift-to-S3 access rather than
embedding long-lived AWS keys.
