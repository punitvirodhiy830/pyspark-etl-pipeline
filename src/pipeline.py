from config import INPUT_FILE
from extract import extract_data
from load import load_data
from logger import get_logger
from spark_session import create_spark_session
from transform import transform_data
from validate import validate_data


logger = get_logger("ecommerce_pipeline")


def run_pipeline():
    """Run the complete e-commerce ETL pipeline."""

    spark = create_spark_session()

    try:
        logger.info("ETL pipeline started.")

        # 1. Extract
        logger.info("Starting data extraction.")
        raw_df = extract_data(spark, INPUT_FILE)
        logger.info("Raw records: %s", raw_df.count())

        # 2. Transform
        logger.info("Starting data transformation.")
        transformed_df = transform_data(raw_df)
        logger.info(
            "Transformed records: %s",
            transformed_df.count()
        )

        # 3. Validate
        logger.info("Starting data validation.")
        validate_data(transformed_df)
        logger.info("Data validation passed.")

        # 4. Load
        logger.info("Loading data into PostgreSQL.")
        load_data(transformed_df)

        logger.info("ETL pipeline completed successfully.")

    except Exception:
        logger.exception("ETL pipeline failed.")
        raise

    finally:
        spark.stop()
        logger.info("Spark session stopped.")


if __name__ == "__main__":
    run_pipeline()