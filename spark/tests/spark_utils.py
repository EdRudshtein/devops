from pyspark.sql import SparkSession


def get_session(hostname: str, port: int) -> SparkSession:
	result=SparkSession.builder\
		.appName("main")\
		.config("spark.driver.bindAddress", hostname)\
		.config("spark.ui.port", str(port))\
		.getOrCreate()
	result.sparkContext.setLogLevel('ERROR')
	return result
