from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "data-engineering",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="ecommerce_pyspark_etl",
    default_args=default_args,
    description="Daily PySpark ETL pipeline for e-commerce orders",
    start_date=datetime(2026, 9, 1),
    schedule="@daily",
    catchup=False,
    tags=["pyspark", "postgresql", "etl"],
) as dag:

    run_pyspark_pipeline = BashOperator(
        task_id="run_pyspark_pipeline",
        bash_command="python /path/to/project/src/pipeline.py",
    )

    run_pyspark_pipeline