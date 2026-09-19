import pytest
from pyspark.sql import SparkSession

from src.validate import validate_data


def test_validate_valid_data():
    spark = (
        SparkSession.builder
        .master("local[2]")
        .appName("test-validation")
        .getOrCreate()
    )

    data = [
        (
            1001,
            "2026-09-01",
            "C001",
            "Aarav Sharma",
            "India",
            "P101",
            "Wireless Mouse",
            "Electronics",
            2,
            799.0,
            "Completed",
            1598.0,
        )
    ]

    columns = [
        "order_id",
        "order_date",
        "customer_id",
        "customer_name",
        "country",
        "product_id",
        "product_name",
        "category",
        "quantity",
        "unit_price",
        "status",
        "total_amount",
    ]

    df = spark.createDataFrame(data, columns)

    assert validate_data(df) is True

    spark.stop()


def test_validate_invalid_quantity():
    spark = (
        SparkSession.builder
        .master("local[2]")
        .appName("test-invalid-quantity")
        .getOrCreate()
    )

    data = [
        (
            1002,
            "2026-09-01",
            "C002",
            "Test User",
            "India",
            "P102",
            "Keyboard",
            "Electronics",
            0,
            1000.0,
            "Completed",
            0.0,
        )
    ]

    columns = [
        "order_id",
        "order_date",
        "customer_id",
        "customer_name",
        "country",
        "product_id",
        "product_name",
        "category",
        "quantity",
        "unit_price",
        "status",
        "total_amount",
    ]

    df = spark.createDataFrame(data, columns)

    with pytest.raises(ValueError):
        validate_data(df)

    spark.stop()