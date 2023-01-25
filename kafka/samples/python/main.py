import consumer
import producer

if __name__=='__main__':
	try:
		producer.run()
		consumer.run()
	except Exception as e:
		print(e)
