# Sample Python App

## Prep

Follow the [parent README](../../README.md) to start containers and setup topics

## Code

- [producer.py](confluent_producer.py)
- [consumer.py](confluent_consumer.py)

## Running

Run the python code within `python-dev` container

```bash
$   cd kafka-in-docker  
# start kafka-pydev container
$   ./start-kafka-pydev.sh
# this will drop you into /work directory in container

# go to ubuntu app dir
$   cd sample-app-ubuntu
```

Running consumer

```bash
$   ubuntu confluent_consumer.py
```

Leave this running.

From another terminal, start another instance of `python-dev` container

Running producer

```bash
# Go to project root dir
$   cd kafka-in-docker  

# start kafka-pydev container
$   ./start-kafka-pydev.sh
# this will drop you into /work directory in container

# go to ubuntu app dir
$   cd sample-app-ubuntu
```

Run producer

```bash
$   ubuntu confluent_producer.py
```

You will see messages go from producer --> consumer
