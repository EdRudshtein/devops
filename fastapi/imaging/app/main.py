from typing import Union

from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def read_root():
	return {"result":"Hello World"}

@app.get("/version")
def read_root():
	return {"result":"1.8"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
	description=f'description of item {item_id}'
	return {"item_id":item_id,"description":description}
