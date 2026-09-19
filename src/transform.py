from pyspark.sql import DataFrame
from pyspark.sql.functions import col, trim, to_date


def transform_data(df: DataFrame) -> DataFrame:
    """Clean and transform raw e-commerce data using PySpark."""

    # Clean text columns
    text_columns = [
        "customer_name",
        "country",
        "product_name",
        "category",
        "status"
    ]

    for column_name in text_columns:
        df = df.withColumn(
            column_name,
            trim(col(column_name))
        )

    # Convert data types
    df = df.withColumn(
        "order_date",
        to_date(col("order_date"), "yyyy-MM-dd")
    )

    df = df.withColumn(
        "quantity",
        col("quantity").cast("integer")
    )

    df = df.withColumn(
        "unit_price",
        col("unit_price").cast("double")
    )

    # Remove records with missing critical fields
    df = df.dropna(
        subset=[
            "order_id",
            "customer_id",
            "product_id",
            "order_date",
            "quantity",
            "unit_price"
        ]
    )

    # Remove invalid business values
    df = df.filter(
        (col("quantity") > 0) &
        (col("unit_price") >= 0)
    )

    # Create derived column
    df = df.withColumn(
        "total_amount",
        col("quantity") * col("unit_price")
    )

    # Remove duplicate order-product records
    df = df.dropDuplicates(
        ["order_id", "product_id"]
    )

    return df