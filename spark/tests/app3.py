#%%
import pyspark
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('app3').getOrCreate()
print(spark)

#%%
