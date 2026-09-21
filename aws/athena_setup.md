# Amazon Athena Setup

1. Open Athena and choose the Glue Data Catalog database.
2. Ensure the processed/analytics S3 locations have been crawled or create
   external tables manually.
3. Run SQL against the S3-backed tables.
4. Store Athena query results in a dedicated S3 results prefix.

Athena is useful for ad-hoc analysis without first loading every dataset
into Redshift.
