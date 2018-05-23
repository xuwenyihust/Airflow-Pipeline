from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from collect import collect_from_topic


default_args = {
                'owner': 'airflow',
                'depends_on_past': False,
                'start_date': datetime(2018, 5, 15),
                'email': ['airflow@example.com'],
                'email_on_failure': False,
                'email_on_retry': False,
                'retries': 1,
                'retry_delay': timedelta(minutes=5),
                }


dag = DAG('zhihu-v0', schedule_interval=timedelta(hours=1), catchup=False, default_args=default_args)

topic_ids = {"exercise": 19552706, "science": 19556664, "history": 19551077, "internet": 19550517}

for topic_name, topic_id in topic_ids.items():
    task = PythonOperator(task_id='collect_from_topic_'+topic_name,
                          python_callable=collect_from_topic,
                          op_args=[topic_id],
                          provide_context=False,
                          dag=dag)
