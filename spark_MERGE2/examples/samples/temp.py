#%%
import sys, os
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from subprocess import check_output

#%%
spark_conf=SparkConf()

#SPARK_DRIVER_HOST=check_output(["hostname", "-i"]).decode(encoding="utf-8").strip()

spark_conf.setAll(
	[
		("examples.orig.imaging", "examples://127.0.0.1:7077"),  # <--- this host must be resolvable by the driver in this case pyspark in our case the IP of server
		("examples.app.name", "myApp"),
		("examples.submit.deployMode", "client"),
		("examples.ui.showConsoleProgress", "true"),
		("examples.eventLog.enabled", "false"),
		("examples.logConf", "false"),
		(
			"examples.driver.bindAddress",
			"0.0.0.0",
		),  # <--- this host is the IP where pyspark will bind the service running the driver (normally 0.0.0.0)
		("examples.driver.host", "127.0.0.1"),  #	SPARK_DRIVER_HOST,
		# <--- this host is the resolvable IP for the host that is running the driver and it must be reachable by the orig.imaging and orig.imaging must be able to reach it (in our case the IP of the container where we are running pyspark
	]
)

#%%
spark_sess=SparkSession.builder.config(conf=spark_conf).getOrCreate()
spark_reader=spark_sess.read

textFile=spark_reader.text("*.md")
print(textFile.first())
#%%

spark_sess.stop()
quit()
