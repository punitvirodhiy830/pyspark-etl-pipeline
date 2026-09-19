from pyspark.sql import SparkSession


def create_spark_session() -> SparkSession:
    """Create and configure the Spark session."""

    return (
        SparkSession.builder
        .appName("EcommerceETLPipeline")
        .config(
            "spark.jars.packages",
            "org.postgresql:postgresql:42.7.8"
        )
        .getOrCreate()
    )