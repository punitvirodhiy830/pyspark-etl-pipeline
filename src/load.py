from pyspark.sql import DataFrame

from config import (
    POSTGRES_URL,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    TARGET_TABLE,
)


def load_data(df: DataFrame) -> None:
    """Load transformed data into PostgreSQL."""

    if not POSTGRES_PASSWORD:
        raise ValueError(
            "POSTGRES_PASSWORD environment variable is not set."
        )

    postgres_properties = {
        "user": POSTGRES_USER,
        "password": POSTGRES_PASSWORD,
        "driver": "org.postgresql.Driver",
    }

    (
        df.write
        .mode("append")
        .jdbc(
            url=POSTGRES_URL,
            table=TARGET_TABLE,
            properties=postgres_properties,
        )
    )

    print(
        f"Successfully loaded {df.count()} rows "
        f"into PostgreSQL table: {TARGET_TABLE}"
    )