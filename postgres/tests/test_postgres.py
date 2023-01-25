from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

import pytest


@pytest.fixture(scope='session')
def engine() -> Engine:
	connection_string="postgresql://postgres:postgres@localhost:5432/temp"
	result=create_engine(connection_string)
	return result


def test_postgres_simple(engine):
	# db_string="postgresql://egr:egr@localhost:5432/main"
	# db=create_engine(db_string)

	# Create
	engine.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")
	engine.execute("INSERT INTO films (title, director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

	# Read
	result_set=engine.execute("SELECT * FROM films")
	for r in result_set:
		print(r)

	engine.execute("UPDATE films SET title='Some2016Film' WHERE year='2016'")
	engine.execute("DELETE FROM films WHERE year='2016'")
