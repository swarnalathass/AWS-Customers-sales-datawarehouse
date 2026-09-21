# Customer & Sales Data Warehouse on AWS

End-to-end data engineering project demonstrating cloud storage, ETL,
data transformation, data warehousing, and analytical SQL using AWS.

## Architecture

Raw CSV Data
    -> Amazon S3 (Raw Zone)
    -> AWS Glue + PySpark
    -> Amazon S3 (Processed/Analytics Zone)
    -> Amazon Redshift (Warehouse)
    -> SQL Analytics

Amazon Athena can query the S3-backed processed data directly.

## Technology Stack

- Python
- SQL
- PySpark
- Amazon S3
- AWS Glue
- Amazon Redshift
- Amazon Athena

## Project Goals

- Build a cloud-based data lake and warehouse workflow.
- Clean and transform customer, product, order, and order-item datasets.
- Produce curated Parquet data.
- Model analytical data using fact and dimension tables.
- Analyze revenue, customers, products, categories, and sales trends.

## Repository Structure

data/          Sample source datasets
pyspark/       PySpark ETL and transformation scripts
sql/           Warehouse DDL and analytics queries
aws/           AWS setup guides
architecture/  Architecture documentation
screenshots/   Place AWS console screenshots here

## Local Quick Start

The PySpark scripts are written for AWS/S3 paths. For a local Spark setup,
replace the S3 paths with local paths and ensure PySpark is installed.

Example:
    spark-submit pyspark/data_cleaning.py

## AWS Deployment Outline

1. Create an S3 bucket and upload the raw CSV data.
2. Create an AWS Glue Catalog database and crawlers.
3. Run an AWS Glue PySpark ETL job.
4. Write processed data to S3 in Parquet format.
5. Crawl the processed data or create Athena external tables.
6. Create Redshift tables using sql/create_tables.sql.
7. Load curated data into Redshift.
8. Run sql/analytics_queries.sql for business analysis.

## Important

This repository contains sample data and template AWS scripts. Before
deployment, replace bucket names, IAM role names, regions, and connection
settings with values from your own AWS account.

Never commit AWS access keys, passwords, or other secrets to GitHub.

## Resume Summary

Built a cloud-based data warehouse to process customer, product, and sales
data using AWS S3, Glue, PySpark, Redshift, Athena, Python, and SQL.
