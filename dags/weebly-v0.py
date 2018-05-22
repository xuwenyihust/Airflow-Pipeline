from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from src.get_customer_summary import get_customer_summary
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

stale_data_path = os.path.join(os.path.dirname(__file__), '../data/weebly/out/*')
task_clean_stale_data = BashOperator(task_id='clean_stale_data',
                                     bash_command='rm -r ' + stale_data_path,
                                     dag=weebly_pipeline)

task_get_customer_summary = PythonOperator(task_id='get_customer_summary',
                                           python_callable=get_customer_summary,
                                           provide_context=False,
                                           dag=weebly_pipeline)

task_get_customer_summary.set_upstream(task_clean_stale_data)
