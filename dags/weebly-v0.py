from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from src.get_customer_summary import get_customer_summary

current_date = datetime.now()

default_args = {
                'owner': 'airflow',
                'depends_on_past': False,
                'start_date': datetime(int(current_date.year), \
                                       int(current_date.month), \
                                       int(current_date.date), \
                                       int(current_date.hour), \
                                       int(current_date.minute)),
                'email': ['airflow@example.com'],
                'email_on_failure': False,
                'email_on_retry': False,
                'retries': 1,
                'retry_delay': timedelta(minutes=5)
                }

dag = DAG('weebly-v0', schedule_interval="@once", catchup=False, default_args=default_args)

task_get_customer_summary = PythonOperator(task_id='get_customer_summary',
                                           python_callable=get_customer_summary,
                                           provide_context=False,
                                           dag=dag)
