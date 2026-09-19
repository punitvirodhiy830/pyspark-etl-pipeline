# E-Commerce PySpark ETL Pipeline

An end-to-end Data Engineering project using PySpark, PostgreSQL and Apache Airflow.

## Architecture

Raw CSV
↓
PySpark Extract
↓
PySpark Transform
↓
Data Quality Validation
↓
PostgreSQL

Airflow → Orchestrates the pipeline

## Tech Stack

- Python
- PySpark
- PostgreSQL
- Apache Airflow
- SQL
- Pytest
- Git/GitHub

## Features

- PySpark-based ETL
- Data cleaning and transformation
- Data type conversion
- Null validation
- Duplicate removal
- Business-rule validation
- Incremental processing using watermark
- PostgreSQL data loading
- Logging and error handling
- Airflow scheduling
- Automated tests with Pytest

## Project Structure

pyspark-etl-pipeline/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── .gitkeep
│   └── orders.csv
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── spark_session.py
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   ├── pipeline.py
│   ├── watermark.py
│   └── logger.py
│
├── sql/
│   ├── schema.sql
│   └── watermark.sql
│
├── airflow/
│   └── dags/
│       └── ecommerce_pipeline.py
│
└── tests/
    ├── test_transform.py
    └── test_validate.py

## ETL Flow

1. Extract raw order data from CSV using PySpark.
2. Clean and transform the data.
3. Perform data-quality checks.
4. Load validated data into PostgreSQL.
5. Use Airflow to schedule and orchestrate the pipeline.

## Data Quality Checks

- Dataset must not be empty
- Required columns must exist
- Critical fields cannot be null
- Quantity must be greater than zero
- Unit price cannot be negative
- Total amount cannot be negative

## Incremental Processing

The project includes a watermark mechanism that tracks the latest processed order date so that future pipeline runs can process only new records.

## Testing

Pytest is used to test:

- PySpark transformations
- Data validation

## How to Run

Install dependencies:

pip install -r requirements.txt

Set PostgreSQL environment variables:

POSTGRES_URL=jdbc:postgresql://localhost:5432/ecommerce

POSTGRES_USER=postgres

POSTGRES_PASSWORD=your_password

TARGET_TABLE=orders

Run the pipeline:

python src/pipeline.py

Run tests:

pytest