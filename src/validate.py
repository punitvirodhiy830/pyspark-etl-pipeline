from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def validate_data(df: DataFrame) -> bool:
    """Run data quality checks on transformed data."""

    # Check 1: Dataset must not be empty
    if df.limit(1).count() == 0:
        raise ValueError("Validation failed: dataset is empty.")

    # Check 2: Required columns must exist
    required_columns = {
        "order_id",
        "order_date",
        "customer_id",
        "product_id",
        "quantity",
        "unit_price",
        "total_amount"
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Validation failed: missing columns {missing_columns}"
        )

    # Check 3: Critical columns cannot contain nulls
    critical_columns = [
        "order_id",
        "order_date",
        "customer_id",
        "product_id",
        "quantity",
        "unit_price",
        "total_amount"
    ]

    null_condition = None

    for column_name in critical_columns:
        condition = col(column_name).isNull()

        if null_condition is None:
            null_condition = condition
        else:
            null_condition = null_condition | condition

    null_count = df.filter(null_condition).count()

    if null_count > 0:
        raise ValueError(
            f"Validation failed: {null_count} records contain null values."
        )

    # Check 4: Quantity must be positive
    invalid_quantity = df.filter(
        col("quantity") <= 0
    ).count()

    if invalid_quantity > 0:
        raise ValueError(
            f"Validation failed: {invalid_quantity} invalid quantity records."
        )

    # Check 5: Unit price cannot be negative
    invalid_price = df.filter(
        col("unit_price") < 0
    ).count()

    if invalid_price > 0:
        raise ValueError(
            f"Validation failed: {invalid_price} negative price records."
        )

    # Check 6: Total amount cannot be negative
    invalid_total = df.filter(
        col("total_amount") < 0
    ).count()

    if invalid_total > 0:
        raise ValueError(
            f"Validation failed: {invalid_total} invalid total amounts."
        )

    print("All data quality checks passed.")
    return True