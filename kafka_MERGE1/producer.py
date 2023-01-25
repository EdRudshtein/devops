import time
from kafka import KafkaProducer
from kafka.producer.future import RecordMetadata

msg=('kafkakafkakafka' * 20).encode('utf-8')[:100]
size=1000000


def kafka_python_producer_sync(producer, size):
	for _ in range(size):
		future=producer.send('topic', msg)
		result=future.get(timeout=60)
	producer.flush()


def success(metadata):
	print(metadata.topic)


def error(exception):
	print(exception)


def kafka_python_producer_async(producer, size):
	for _ in range(size):
		producer.send('topic', msg).add_callback(success).add_errback(error)
	producer.flush()


producer=KafkaProducer(bootstrap_servers='localhost:9092')
future=producer.send('topic', f'hello0'.encode('utf-8'))
result=future.get(timeout=60)  # type: RecordMetadata
print(result.offset)
producer.flush()
