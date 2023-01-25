from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def helloWorld()->int:
	print('Hello World')
	return 0


with DAG(dag_id="dag1",start_date=datetime(2021,1,1),schedule_interval="@hourly",catchup=False) as dag:
	task1=PythonOperator(task_id="hello_world",python_callable=helloWorld)
