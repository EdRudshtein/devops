#%%
from pyspark.sql import SparkSession

#%%
spark=SparkSession.builder.appName("sparkanalysis")\
	.config("examples.jars", "postgresql-42.2.22.jar")\
	.getOrCreate()

#%%
pgDF=spark.read\
	.format("jdbc")\
	.option("url", "jdbc:postgresql://127.0.0.1:5432/postgres")\
	.option("dbtable", "public.states")\
	.option("user", "postgres")\
	.option("password", "casa1234")\
	.option("driver", "org.postgresql.Driver")\
	.load()

#%%
df=spark.read.format("jdbc").option("url", "jdbc:postgresql://localhost:5432/postgres")\
	.option("driver", "org.postgresql.Driver").option("dbtable", "states")\
	.option("examples.jars", "/opt/examples-apps/postgresql-42.2.22.jar")\
	.option("user", "postgres").option("password", "casa1234").load()

#%%
df.toDF().head()
