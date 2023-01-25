from cassandra.cluster import Cluster, Session
from cassandra.auth import PlainTextAuthProvider
import logging
import pytest


def create_session() -> Session:
	auth_provider=PlainTextAuthProvider(username='cassandra', password='cassandra')
	cluster=Cluster(auth_provider=auth_provider)
	session=cluster.connect()
	#	print(type(session))
	return session


def create_keyspace(session: Session, keyspace: str) -> None:
	logging.info("creating keyspace")
	sql=f"""
		CREATE KEYSPACE IF NOT EXISTS {keyspace}
		WITH replication = {{'class': 'SimpleStrategy', 'replication_factor': '1' }};
		"""
	session.execute(sql)


def drop_keyspace(session: Session, keyspace: str) -> None:
	logging.info("dropping keyspace")
	sql=f'drop keyspace {keyspace};'
	session.execute(sql)


def test_full():
	session=create_session()
	create_keyspace(session, "temp")
	drop_keyspace(session, "temp")


# auth_provider=PlainTextAuthProvider(username='cassandra', password='cassandra')
# cluster=Cluster(auth_provider=auth_provider)
# session=cluster.connect()
# print(session)


if __name__=='__main__':
	try:
		logging.basicConfig(encoding='utf-8', level=logging.INFO)
		test_full()
		print('success')
	except Exception as e:
		print(e)

#%%

# query=SimpleStatement("""
#     INSERT INTO mytable (thekey, col1, col2)
#     VALUES (%(key)s, %(age)s, %(b)s)
#     """, consistency_level=ConsistencyLevel.ONE)
#
# prepared=session.prepare("""
#     INSERT INTO mytable (thekey, col1, col2)
#     VALUES (?, ?, ?)
#     """)
#
# for i in range(10):
# 	print("inserting row %d" % i)
# 	session.execute(query, dict(key="key%d" % i, a='age', b='b'))
# 	session.execute(prepared, ("key%d" % i, 'b', 'b'))
