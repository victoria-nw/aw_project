# NYC Taxi Data Pipeline

A production-style data pipeline built on Azure Databricks using the medallion architecture (Bronze → Silver → Gold).

## Tech Stack
- Azure Databricks
- Azure Data Lake Storage Gen2 (ADLS)
- Delta Lake
- Unity Catalog
- Azure DevOps (CI/CD)

## Pipeline Layers
- **Bronze** – Raw ingestion from NYC TLC trip data
- **Silver** – Cleaned, deduplicated, transformed data
- **Gold** – Aggregated, business-ready tables

## Data Source
NYC TLC Trip Record Data – Yellow Taxi (2023)
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page