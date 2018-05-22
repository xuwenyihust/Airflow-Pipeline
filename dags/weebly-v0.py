from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from src.get_customer_summary import get_customer_summary

current_date = datetime.utcnow() - timedelta(days=1)

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

weebly_pipeline = DAG('weebly-v0', schedule_interval="@once", catchup=False, default_args=default_args)

def write():
    output_path = os.path.join(os.path.dirname(__file__), '../data/weebly/out/test.csv')
    f_out.write("233333333")

task_write = PythonOperator(task_id='get_customer_summary',
                            python_callable=write,
                            provide_context=False,
                            dag=weebly_pipeline)

# task_get_customer_summary = PythonOperator(task_id='get_customer_summary',
#                                            python_callable=get_customer_summary,
#                                            provide_context=False,
#                                            dag=weebly_pipeline)
