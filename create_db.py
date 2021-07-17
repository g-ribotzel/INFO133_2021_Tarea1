from bson.binary import Binary
import pymongo
from pymongo import MongoClient

MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_DB = "fusaDB"

myclient = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
mydb = myclient[MONGO_DB]
mycol = mydb['grabaciones']


mycol.delete_many({})

many = list()

many.append({ 
"ID":"0001",
"fecha de grabacion":"25/06/2020",
"ciudad":"Valdivia",
"duracion":"00:32",
"formato":"WAV",
"latitud":-39.814068,
"longitud":-73.248934,
"exterior":"Exterior",
"usuario": {"RUT":"24000500-2", "nombre":"Maicol", "apellido":"Lico" },
"segmentos":[
    { "ID":"0012", 
    "formato":"wav", 
    "duracion":"00:32", 
    "inicio":"00:05", 
    "fin":"00:10",
    "etiquetas": [{"nombre_fuente":"Animales", "descripcion":"Canto de gaviotas", "id_analizador":"20A"}]
 }]
})

many.append({ 
"ID":"1069",
"fecha de grabacion":"09/11/2020",
"ciudad":"Valdivia",
"duracion":"00:45",
"formato":"WAV",
"latitud":-39.829542,
"longitud":-73.234537,
"exterior":"Exterior",
"usuario": {"RUT":"10521500-2", "nombre":"Baldomero", "apellido":"Pitanzas" },
"segmentos":[
    { "ID":"0025", 
    "formato":"wav", 
    "duracion":"00:12", 
    "inicio":"00:05", 
    "fin":"00:17",
    "etiquetas": [{"nombre_fuente":"Vehiculos", "descripcion":"trafico vehicular", "id_analizador":"18H"}]
 }]
})

many.append({ 
"ID":"0550",
"fecha de grabacion":"09/11/2020",
"ciudad":"Valdivia",
"duracion":"00:30",
"formato":"WAV",
"latitud":-39.819587,
"longitud":-73.230560,
"exterior":"Exterior",
"usuario": {"RUT":"18900032-7", "nombre":"Cristina", "apellido":"Angustiada" },
"segmentos":[
    { "ID":"0059", 
    "formato":"wav", 
    "duracion":"00:15", 
    "inicio":"00:15", 
    "fin":"00:30",
    "etiquetas": [{"nombre_fuente":"Animales", "descripcion":"varios perros ladrando", "id_analizador":"05H"}]
 }]
})

many.append({ 
"ID":"0420",
"fecha de grabacion":"02/03/2021",
"ciudad":"Valdivia",
"duracion":"00:20",
"formato":"WAV",
"latitud":-39.830706,
"longitud":-73.239402,
"exterior":"Interior",
"usuario": {"RUT":"9002131-K", "nombre":"Lautaro", "apellido":"Gutierrez" },
"segmentos":[
    { "ID":"0102", 
    "formato":"wav", 
    "duracion":"00:10", 
    "inicio":"00:00", 
    "fin":"00:10",
    "etiquetas": [{"nombre_fuente":"Humanos", "descripcion":"personas camniando y hablando dentro de un consultorio", "id_analizador":"06A"}]
 }]
})


mycol.insert_many(many)
for x in mycol.find():
  print(x)
print(mycol.count_documents({}))

