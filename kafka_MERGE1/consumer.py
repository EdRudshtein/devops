from kafka import KafkaConsumer, TopicPartition

size=1000000


def run_consumer_1(consumer: KafkaConsumer) -> None:
	consumer.subscribe(['topic'], )
	for msg in consumer:
		print(msg.value.decode('utf-8'))


def run_consumer_2(consumer):
	consumer.assign([TopicPartition('topic1', 1), TopicPartition('topic2', 1)])
	for msg in consumer:
		print(msg)


def run_consumer_3(consumer):
	partition=TopicPartition('topic3', 0)
	consumer.assign([partition])
	last_offset=consumer.end_offsets([partition])[partition]
	for msg in consumer:
		if msg.offset==last_offset-1:
			break


consumer=KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='earliest')

run_consumer_1(consumer)
# consumer2=KafkaConsumer(bootstrap_servers='localhost:9092')
# consumer3=KafkaConsumer(bootstrap_servers='localhost:9092')
