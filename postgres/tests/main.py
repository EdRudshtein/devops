from sqlalchemy import create_engine


def run():
	db_string="postgresql://egr:egr@localhost:5432/main"
	engine=create_engine(db_string)
	engine.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
	engine.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")
	result_set=engine.execute("SELECT * FROM films")
	for r in result_set:
		print(r)
	engine.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")
	engine.execute("DELETE FROM films WHERE year='2016'")
	pass


if __name__=='__main__':
	try:
		run()
	except Exception as e:
		print(e)
