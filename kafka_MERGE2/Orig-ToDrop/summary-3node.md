# Quickstart - Multi Node Kafka

## Overview


This stack has:

- 1 Zookeeper
- 3 Kafka brokers
- Kafka UI Manager

## Step-1: Build Custom Docker Images

Only need to do this once.

```bash
$   cd  kafka-in-docker
$   bash ./build-images.sh
```

## Step-2: Start the stack

```bash
$   bash start-kafka-3node.sh
```

## Step-3: Login to a Kafka broker

Login to a kafka node

```bash
$   docker-compose  -f docker-compose-kafka-3node.yaml  exec  kafka1  bash
```

## Step-4: Create a Test Topic

We do this **within the `kafka1` container**, we just started.

```bash
# See current topics
$    kafka-topics.sh --bootstrap-server kafka1:19092  --list

# Create a new topic
$   kafka-topics.sh--bootstrap-server kafka1:19092   \
       --create --topic test --replication-factor 3  --partitions 10

# Describe topic
$   kafka-topics.sh--bootstrap-server kafka1:19092   \
       --describe --topic test 
```

## Step-5: Start Console Consumer

We do this **within the `kafka1` container**, we just started.

```bash
$    kafka-console-consumer.sh  --bootstrap-server kafka1:19092   \
         --property print.key=true --property key.separator=":"  --topic test

```

Note, our kafka bootstrap server is `kafka1:19092`, this is the advertised kafka broker address in docker network.

## Step-6: Start Console Producer

On another terminal, login to another Kafka node

```bash
$   docker-compose -f docker-compose-kafka-3node.yaml  exec kafka2  bash
```

Within the kafka container, start the console producer

Run producer

```bash
$    kafka-console-producer.sh --bootstrap-server kafka2:19092  --topic test
```

Type a few lines into console producer terminal

```text
1
2
3
4
```

And watch it come out on console terminal

## Step-7: Kafka Manager UI

Access Kafka Manager UI on url : [http://localhost:9000](http://localhost:9000)

Register our new Kafka cluster as follows

![](../images/kafka-manager-1.png)

Once registered, you will see topics and brokers displayed like this.

![](../images/kafka-multi-1.png)

Click on the brokers, and you will see broker details.  You can also see JMX metrics are published!

![](../images/kafka-multi-2.png)

Click on broker id, to see more detailed stats on a broker.

![](../images/kafka-multi-3.png)

## Step-8: Developing Applications

Let's develop a sample app in Java and Python.

## Step-9: Java App

We have a sample Java app in [work/sample-app-java](../../samples/kafka/java/)

And we have a java development environent ready!  You don't even need to have Java or Maven installed on your computer :-) 

Start Java dev env:

```bash
$   cd kafka-in-docker
$   bash ./start-java-dev.sh
```

This will drop you into `work` directory in the container.

The following commands are executed in Java container

```bash
$   cd java

# build the Java app
$   mvn  clean package

# Run Java consumer
$    java -cp target/hello-kafka-1.0-jar-with-dependencies.jar   x.SimpleConsumer
```

## Step-10: Python app

We have a sample python app in [work/sample-app-python](work/sample-app-python/)

From another terminal, start python-dev environment

```bash
$   cd kafka-in-docker
$   bash ./start-kafka-pydev.sh
```

Within python container, try these

```bash
# we are currently in /work directory
$   cd sample-app-ubuntu

# run producer
$   ubuntu  confluent_producer.py
```

Now, observe output on console-consumer and java-consumer windows!  And check-out the Kafka-manager UI too.

![](../images/kafka-single-5a.png)

## Step-11: Shutdown

```bash
$   bash ./stop-kafka-3node.sh
```
