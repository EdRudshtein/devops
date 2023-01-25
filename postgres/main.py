import os

import psycopg2
from psycopg2.extensions import connection

pg_password=os.environ['POSTGRES_PASSWORD']


def get_connection() -> connection:
	result=psycopg2.connect(user="egr", password=pg_password, host="127.0.0.1", port="5432", database="main")
	return result


def create(conn: connection):
	cursor=conn.cursor()
	query="""
		CREATE TABLE IF NOT EXISTS states (
		   id SERIAL PRIMARY KEY,
		   symbol TEXT NOT NULL UNIQUE,
		   description TEXT NOT NULL UNIQUE
		);	    
	"""
	cursor.execute(query)
	conn.commit()
	query="""
        INSERT INTO states (symbol,description) VALUES ('FL','Florida');
        INSERT INTO states (symbol,description) VALUES ('NY','New York');
    """
	cursor.execute(query)
	conn.commit()
	cursor.close()


def read(conn: connection):
	cursor=conn.cursor()
	cursor.execute("SELECT * from states")
	record=cursor.fetchall()
	print(record)
	cursor.close()


def run():
	connection=get_connection()
	print(type(connection))
	read(connection)
	connection.close()


if __name__=='__main__':
	try:
		conn=get_connection()
		#		print(type(connection))
#		create(conn)
		read(conn)
		conn.close()
	except Exception as e:
		print(e)
