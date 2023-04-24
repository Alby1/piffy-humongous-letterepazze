from fastapi import FastAPI
from pymongo import MongoClient
from pandas import DataFrame
from fastapi import FastAPI
import uvicorn

app = FastAPI()


def get_database():
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb://localhost/"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['US']

   
  
@app.get("/")
async def root():
   dbname = get_database()

   cities = dbname['US']
   cc = cities.find().limit(5)
   #cc = DataFrame(cc)
   print(cc)
   return cc
  
if __name__ == "__main__":   
   uvicorn.run("main:app", port=7300, reload=True)
   
   
