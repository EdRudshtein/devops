#%%
from pyspark.sql import SparkSession
import pandas as pd

#%%
spark=SparkSession.builder\
	.master("spark://127.0.0.1:7077")\
	.appName("SimpleApp")\
	.getOrCreate()
print(spark)
# .config("spark.shuffle.service.enabled", "false")\
# .config("spark.dynamicAllocation.enabled", "false")\
# .config("driver-memory", "5g")\
# .config("executor-memory", "5g")\
# .config("executor-cores", "2")\

#%%
filename="data/story.txt"  # Should be some file on your system
text=spark.read.text(filename).cache()
# noinspection PyTypeChecker
pdf=text.toPandas()  # type: pd.DataFrame

#%%
print(pdf.head(10))

#%%
numAs=text.filter(text.value.contains('a')).count()
numBs=text.filter(text.value.contains('b')).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

#%%
spark.stop()
