import json
from airflow import DAG
from datetime import datetime
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from pandas import json_normalize

with DAG(dag_id="main1",start_date=datetime(2022,9,20),schedule_interval="@daily",catchup=False) as dag:
	create_table=PostgresOperator(
		task_id='create_table',
		postgres_conn_id='conn1',
		sql='''
			CREATE TABLE IF NOT EXISTS users1 (
				first_name TEXT NOT NULL,
				last_name TEXT NOT NULL,
				email TEXT NOT NULL
			)
		'''
	)

	is_api_available=HttpSensor(
		task_id='is_api_available',
		http_conn_id='user_api',
		endpoint='api/')

	extract_user=SimpleHttpOperator(
		task_id='extract_user',
		http_conn_id='user_api',
		endpoint='api/',
		method='GET',
		response_filter=lambda response:json.loads(response.text),
		log_response=True
	)


	def process_user_handle(ti):
		print(f"task_id is '{ti.task_id}'")
		user=ti.xcom_pull(task_ids="extract_user")
		user=user['results'][0]
		processed_user=json_normalize({
			'firstname':user['name']['first'],
			'lastname':user['name']['last'],
			'country':user['location']['country'],
			'username':user['login']['username'],
			'password':user['login']['password'],
			'email':user['email']})
		processed_user.to_csv('/tmp/processed_user.csv',index=None,header=False)


	process_user=PythonOperator(
		task_id='process_user',
		python_callable=process_user_handle
	)


	def store_user_handle():
		hook=PostgresHook(postgres_conn_id='postgres')
		hook.copy_expert(
			sql="COPY users FROM stdin WITH DELIMITER as ','",
			filename='/tmp/processed_user.csv'
		)


	store_user=PythonOperator(
		task_id='store_user',
		python_callable=store_user_handle
	)

	create_table >> is_api_available >> extract_user >> process_user >> store_user
