from bson import ObjectId
from fastapi import FastAPI
from pymongo import MongoClient
from pandas import DataFrame
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import re

app = FastAPI()


def get_database():
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb://localhost/"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['US']

   
  
@app.get("/lettere")
async def lettere(mittente: str = None):
   dbname = get_database()

   lettere = dbname['lettere']
   cities = dbname['US']
   cc = lettere.find()
   if mittente is not None:
      m = re.compile(f".*{mittente}*.", re.IGNORECASE)
      cc = lettere.find({"mittente": m})
   #cc = DataFrame(cc)
   ccc = []
   for c in cc:
      c["_id"] = str(c["_id"])
      c['arrivo']['citta'] = cities.find_one({"_id" : ObjectId(c['arrivo']['citta'])})
      c['arrivo']['citta']["_id"] = str(c['arrivo']['citta']["_id"])
      c['partenza']['citta'] = cities.find_one({"_id" : ObjectId(c['partenza']['citta'])})
      c['partenza']['citta']["_id"] = str(c['partenza']['citta']["_id"])
      ccc.append(c)
   return ccc


@app.get("/")
async def root():
   return FileResponse("index.html")
  
if __name__ == "__main__":   
   uvicorn.run("main:app", port=7300, reload=True)
   
   
