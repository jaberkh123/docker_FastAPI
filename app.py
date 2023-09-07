from fastapi import FastAPI
import requests
app = FastAPI()
'''
fake_items_db = [{"item_name": "mahammaaad reza"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
response = requests.get("http://127.0.0.1:8000/valid")
print(response)
print(response.json())
'''

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
