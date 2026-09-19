from config import INPUT_FILE
from extract import extract_data
from load import load_data
from spark_session import create_spark_session
from transform import transform_data
from validate import validate_data


def run_pipeline():
    """Run the complete e-commerce ETL pipeline."""

    spark = create_spark_session()

    try:
        print("=== E-Commerce ETL Pipeline Started ===")

        # 1. Extract
        print("1. Extracting raw data...")
        raw_df = extract_data(spark, INPUT_FILE)
        print(f"Raw records: {raw_df.count()}")

        # 2. Transform
        print("2. Transforming data...")
        transformed_df = transform_data(raw_df)
        print(f"Transformed records: {transformed_df.count()}")

        # 3. Validate
        print("3. Validating data...")
        validate_data(transformed_df)

        # 4. Load
        print("4. Loading data into PostgreSQL...")
        load_data(transformed_df)

        print("=== Pipeline Completed Successfully ===")

    except Exception as error:
        print(f"=== Pipeline Failed: {error} ===")
        raise

    finally:
        spark.stop()


if __name__ == "__main__":
    run_pipeline()