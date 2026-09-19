from pyspark.sql import DataFrame, SparkSession


def extract_data(
    spark: SparkSession,
    input_file: str
) -> DataFrame:
    """Read raw order data from CSV using PySpark."""

    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(input_file)
    )