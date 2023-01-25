from cassandra.cluster import Cluster,Session


def get_session(keyspace: str) -> Session:
	cluster=Cluster(['127.0.0.1'],port=9042)
	return cluster.connect(keyspace,wait_for_all_pools=True)


def create_table(session: Session) -> None:
	session.execute("""
	        CREATE TABLE IF NOT EXISTS prices (
	            thekey text,
	            col1 text,
	            col2 text,
	            PRIMARY KEY (thekey, col1)
	        )
	        """)
	statement=session.prepare("""
	    INSERT INTO prices (thekey, col1, col2) VALUES (?, ?, ?)
	    """)

	for i in range(10):
		#		print("inserting row %d" % i)
		#		session.execute(query, dict(key="key%d" % i, age='age', b='b'))
		q=session.execute(statement,(f'key{i}','age','b'))
		print(q)
	pass


# def run():
# 	cluster=Cluster(['127.0.0.1'], port=9042)
# 	session=cluster.connect('temp', wait_for_all_pools=True)
# #	session.execute('USE cityinfo')
# 	rows=session.execute('SELECT * FROM table1')
# 	for row in rows:
# 		print(row.name, row.country)

def run():
	session=get_session('temp')
	create_table(session)


if __name__=="__main__":
	try:
		run()
		print('success')
	except Exception as e:
		print(e)
