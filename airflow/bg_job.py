import airflow
from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

PROJECT_ID = "project-b369d3e9-b19b-4338-90a"
LOCATION = "US"

ARGS = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    dag_id="bigquery_dag",
    schedule_interval=None,
    description="DAG to run the bigquery jobs",
    default_args=ARGS,
    tags=["gcs", "bq", "etl"]
) as dag:

    bronze_tables = BigQueryInsertJobOperator(
        task_id="bronze_tables",
        configuration={
            "query": {
                "query": "{% include 'data/bigquery/bronze.sql' %}",
                "useLegacySql": False,
                "priority": "BATCH"
            }
        },
        location=LOCATION,
        project_id=PROJECT_ID
    )

    silver_tables = BigQueryInsertJobOperator(
        task_id="silver_tables",
        configuration={
            "query": {
                "query": "{% include 'data/bigquery/silver.sql' %}",
                "useLegacySql": False,
                "priority": "BATCH"
            }
        },
        location=LOCATION,
        project_id=PROJECT_ID
    )

    gold_tables = BigQueryInsertJobOperator(
        task_id="gold_tables",
        configuration={
            "query": {
                "query": "{% include 'data/bigquery/gold.sql' %}",
                "useLegacySql": False,
                "priority": "BATCH"
            }
        },
        location=LOCATION,
        project_id=PROJECT_ID
    )

bronze_tables >> silver_tables >> gold_tables