from bson.binary import Binary
import pymongo
from pymongo import MongoClient

MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_DB = "fusaDB"

myclient = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
mydb = myclient[MONGO_DB]
mycol = mydb['archivos']

mycol.delete_many({})

model_file = 'Trafico.wav'

with open(model_file, "rb") as f:
    encoded = Binary(f.read())

dic = {"file": encoded,
       "ID":"1069",
       "filename": model_file,
       "description": "Trafico vehicular en la ciudad" }

mycol.insert_one(dic)

model_file = 'Perros.wav'

with open(model_file, "rb") as f:
    encoded = Binary(f.read())

dic = {"file": encoded,
       "ID":"0550",
       "filename": model_file,
       "description": "Perros ladrando en el pasaje" }


mycol.insert_one(dic)

model_file = 'hospital.wav'

with open(model_file, "rb") as f:
    encoded = Binary(f.read())

dic = {"file": encoded,
       "ID":"0420",
       "filename": model_file,
       "description": "Interior de un consultorio" }

mycol.insert_one(dic)

model_file = 'Gaviotas.wav'

with open(model_file, "rb") as f:
    encoded = Binary(f.read())

dic = {"file": encoded,
       "ID":"0001",
       "filename": model_file,
       "description": "Canto de gaviotas" }

mycol.insert_one(dic)


print(mycol.count_documents({}))

