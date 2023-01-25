import time
from kafka import KafkaProducer
from kafka.producer.future import RecordMetadata
from datetime import datetime

msg=('test-' * 20).encode('utf-8')[:100]
size=10


def success(metadata):
	print(metadata.topic)


def error(exception):
	print(exception)


def kafka_python_producer_sync(producer, size):
	for _ in range(size):
		future=producer.send('topic', msg)
		result=future.get(timeout=60)
	producer.flush()


def kafka_python_producer_async(producer, size):
	for _ in range(size):
		producer.send('topic', msg).add_callback(success).add_errback(error)
	producer.flush()


def run():
	producer=KafkaProducer(bootstrap_servers='localhost:9092')
	for i in range(10):
		message=f'hello from EGR - {datetime.now()}'
		print(f'sending {message}')
		future=producer.send('topic', message.encode('utf-8'))
		result=future.get(timeout=60)  # type: RecordMetadata
		print(result.offset)
	producer.flush()
