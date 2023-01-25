#!/usr/bin/python3
import os
from cassandra.cluster import Cluster,Session


def get_session(keyspace: str) -> Session:
	cluster=Cluster(['127.0.0.1'],port=9042)
	return cluster.connect(keyspace,wait_for_all_pools=True)


def create_table(session: Session) -> None:
	# keyspace='temp'
	# cluster=Cluster(['127.0.0.1'], port=9042)
	#	session=cluster.connect('temp', wait_for_all_pools=True)

	#	cluster=Cluster('localhost', port=9042)
	# session=cluster.connect()
	# print("creating keyspace...")
	# session.execute("""
	#     CREATE keyspace IF NOT EXISTS %s
	#     WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
	#     """ % keyspace)
	#
	# cluster=Cluster([os.environ["CASSANDRA_IP_ADDRESS"]], port=9042)
	# session=cluster.connect(keyspace, wait_for_all_pools=True)
	a=session.execute("""
	        CREATE TABLE IF NOT EXISTS table2 (
	            thekey text,
	            col1 text,
	            col2 text,
	            PRIMARY KEY (thekey, col1)
	        )
	        """)
	print(a)


if __name__=='__main__':
	try:
		session=get_session()
		create_table()
	except Exception as e:
		print(e)
