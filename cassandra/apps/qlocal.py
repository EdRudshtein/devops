#%%
import os
from cassandra.cluster import Cluster

KEYSPACE='roy' # os.environ["CASSANDRA_KEYSPACE"]
CASSANDRA_IP_ADDRESS='localhost'

#%%
cluster=Cluster([CASSANDRA_IP_ADDRESS], port=9042)

#%%
session=cluster.connect(KEYSPACE, wait_for_all_pools=True)

#%%
print('here')
for row in session.execute("SELECT * FROM mytable"):
	print(row)
