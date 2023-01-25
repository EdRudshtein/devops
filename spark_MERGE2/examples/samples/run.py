#%%
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format

#%%
spark=SparkSession.builder.appName("trip-app").config("examples.jars", "/opt/jars/postgresql-42.2.22.jar").getOrCreate()
sc=spark.sparkContext
sc.setLogLevel("WARN")

#%%
file="data/MTA-Bus-Time.2014-08-01.csv"
df=sql.read.load(file, format="csv", inferSchema="true", sep="\t", header="true")\
	.withColumn("report_hour", date_format(col("time_received"), "yyyy-MM-dd HH:00:00"))\
	.withColumn("report_date", date_format(col("time_received"), "yyyy-MM-dd"))

#%%
q=df.where("latitude <= 90 AND latitude >= -90 AND longitude <= 180 AND longitude >= -180")
# \
# 	.where("latitude != 0.000000 OR longitude !=  0.000000 ") \
# 	.write \
# 	.jdbc(url=url, table="mta_reports", mode='append', properties=properties) \
# 	.save()

q.show()
#%%
url="jdbc:postgresql://demo-database:5432/mta_data"

properties={
	"user":"postgres",
	"password":"casa1234",
	"driver":"org.postgresql.Driver"
}

#%%
#q.write.jdbc(url=url, table="mta_reports", mode='append', properties=properties).save()

#%%
df=spark.read.format("jdbc").option("url", "jdbc:postgresql://localhost:5432/dezyre_new")\
	.option("driver", "org.postgresql.Driver").option("dbtable", "states")\
	.option("user", "postgres").option("password", "casa1234").load()

#%%
jdbcDF=spark.read\
	.format("jdbc")\
	.option("url", "jdbc:postgresql:dbserver")\
	.option("dbtable", "public.states")\
	.option("user", "postgres")\
	.option("password", "casa1234")\
	.load()
#%%
