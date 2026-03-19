import os

# Storage
STORAGE_ACCOUNT = os.getenv("STORAGE_ACCOUNT", "nyctaxistorage")
LANDING_CONTAINER = os.getenv("LANDING_CONTAINER", "landing")
BRONZE_CONTAINER = os.getenv("BRONZE_CONTAINER", "bronze")
SILVER_CONTAINER = os.getenv("SILVER_CONTAINER", "silver")
GOLD_CONTAINER = os.getenv("GOLD_CONTAINER", "gold")

# ADLS paths
LANDING_PATH = f"abfss://{LANDING_CONTAINER}@{STORAGE_ACCOUNT}.dfs.core.windows.net/"
BRONZE_PATH = f"abfss://{BRONZE_CONTAINER}@{STORAGE_ACCOUNT}.dfs.core.windows.net/"
SILVER_PATH = f"abfss://{SILVER_CONTAINER}@{STORAGE_ACCOUNT}.dfs.core.windows.net/"
GOLD_PATH = f"abfss://{GOLD_CONTAINER}@{STORAGE_ACCOUNT}.dfs.core.windows.net/"

# Unity Catalog
CATALOG_DEV = os.getenv("CATALOG_DEV", "dev")
CATALOG_QA = os.getenv("CATALOG_QA", "qa")
CATALOG_PROD = os.getenv("CATALOG_PROD", "prod")

# Schemas
BRONZE_SCHEMA = "bronze"
SILVER_SCHEMA = "silver"
GOLD_SCHEMA = "gold"