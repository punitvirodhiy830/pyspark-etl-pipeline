from pyspark.sql import SparkSession

from src.transform import transform_data


def test_transform_data():
    spark = (
        SparkSession.builder
        .master("local[2]")
        .appName("test-transform")
        .getOrCreate()
    )

    data = [
        (
            1,
            "2026-09-01",
            "C001",
            " Aarav Sharma ",
            "India",
            "P101",
            " Wireless Mouse ",
            "Electronics",
            2,
            799.0,
            "Completed",
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
    ]

    df = spark.createDataFrame(data, columns)

    result = transform_data(df)

    assert result.count() == 1
    assert result.first()["customer_name"] == "Aarav Sharma"
    assert result.first()["total_amount"] == 1598.0

    spark.stop()