import folium
import playsound
import pymongo
from pymongo import MongoClient

MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_DB = "fusaDB"

fecha = "09/11/2020"

myclient = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
mydb = myclient[MONGO_DB]

#Comienzo Consulta 1

consulta = {"fecha de grabacion":fecha}

mapa = folium.Map(location =[-39.823641, -73.226158], zoom_start = 14)

for x in mydb['grabaciones'].find(consulta):
  nb=mydb["archivos"].find_one({"ID":x["ID"]})
  po="<b>Archivo: "+nb["filename"]+"\nID: "+nb["ID"]+"\nFecha: "+x["fecha de grabacion"]+"</b>"
  folium.Marker([x["latitud"], x["longitud"]], popup=po, tooltip=nb["description"]).add_to(mapa)

mapa.save('consulta1.html')

#Fin Consulta 1

#Comienzo Consulta 2

mapa1 = folium.Map(location =[-39.823641, -73.226158], zoom_start = 14)

consulta = {"segmentos": {"$elemMatch" : {"etiquetas": {"$elemMatch" : {"nombre_fuente":"Animales"} } } } }

for x in mydb["grabaciones"].find(consulta):
    nb=mydb["archivos"].find_one({"ID":x["ID"]})
    po="<b>Archivo: "+nb["filename"]+"\nID: "+nb["ID"]+"\nFecha: "+x["fecha de grabacion"]+"</b>"
    folium.Marker([x["latitud"], x["longitud"]], popup=po, tooltip=nb["description"]).add_to(mapa1)

mapa1.save('consulta2.html')

#Fin Consulta 2

#Reproduccion de audio

data = mydb["archivos"].find_one({"filename":"Trafico.wav"})
with open("temp.wav", "wb") as f:
    f.write(data['file'])

playsound.playsound("temp.wav")

