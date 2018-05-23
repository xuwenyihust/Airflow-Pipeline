from airflow import DAG
from dags import weebly_v0

def test_dag_integrity():
    assert isinstance(weebly_v0.weebly_pipeline, DAG)
