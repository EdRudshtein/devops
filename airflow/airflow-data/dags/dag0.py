from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def helloWorld() -> int:
	print('in helloWorld')
	return _helloWorld()


def _helloWorld() -> int:
	print('in _helloWorld')
	return 3


with DAG(dag_id="dag0",start_date=datetime(2022,12,20),schedule_interval="@daily",catchup=True) as dag:
	task1=PythonOperator(task_id="hello_world",python_callable=helloWorld)
