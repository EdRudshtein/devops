# Apache Spark

### Additional Workers
If you want N workers, all you need to do is start the docker-compose deployment with the following command:

```
docker-compose up --scale spark-worker=3
```


### Installing additional jars
image can be extended to add as many jars as needed for your specific use case.
For instance, the following Dockerfile adds aws-java-sdk-bundle-1.11.704.jar:
```
FROM bitnami/spark
RUN curl https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.704/aws-java-sdk-bundle-1.11.704.jar --output /opt/bitnami/spark/jars/aws-java-sdk-bundle-1.11.704.jar

```