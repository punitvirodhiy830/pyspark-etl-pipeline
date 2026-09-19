from pyspark.sql import DataFrame
from pyspark.sql.functions import col, max as spark_max


def get_latest_order_date(df: DataFrame):
    """Return the latest order date from the dataset."""

    result = df.select(
        spark_max(col("order_date")).alias("latest_order_date")
    ).collect()[0]

    return result["latest_order_date"]


def filter_incremental_data(
    df: DataFrame,
    last_processed_date
) -> DataFrame:
    """Keep only records newer than the last processed date."""

    if last_processed_date is None:
        return df

    return df.filter(
        col("order_date") > last_processed_date
    )