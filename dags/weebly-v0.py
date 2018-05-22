from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from src.get_customer_geo_dist import get_customer_geo_dist
import os

current_date = datetime.utcnow() - timedelta(days=5)

default_args = {
                'owner': 'airflow',
                'depends_on_past': False,
                'start_date': datetime(int(current_date.year), \
                                       int(current_date.month), \
                                       int(current_date.day), \
                                       int(current_date.hour), \
                                       int(current_date.minute)),
                'email': ['airflow@example.com'],
                'email_on_failure': False,
                'email_on_retry': False,
                'retries': 1,
                'retry_delay': timedelta(minutes=5)
                }

weebly_pipeline = DAG('weebly-v0', schedule_interval="@daily", catchup=False, default_args=default_args)

script_path = os.path.join(os.path.dirname(__file__), '../src/clean_stale_data.sh')
clean_stale_data_command = """
. {{params.script_path}}
"""
task_clean_stale_data = BashOperator(task_id='clean_stale_data',
                                     bash_command=clean_stale_data_command,
                                     params={'script_path': script_path},
                                     dag=weebly_pipeline)

task_get_customer_geo_dist = PythonOperator(task_id='get_customer_geo_dist',
                                           python_callable=get_customer_geo_dist,
                                           provide_context=False,
                                           dag=weebly_pipeline)

task_get_customer_geo_dist.set_upstream(task_clean_stale_data)
