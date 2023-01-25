import spark_utils


def main():
	session=spark_utils.get_session('rudshtein.local',7077)
	sc=session.sparkContext
	df=sc.parallelize([1, 2, 3, 4, 5])
	q=df.map(lambda x:x * x).sum()
	print(f'Result: {q}')


if __name__=='__main__':
	main()
