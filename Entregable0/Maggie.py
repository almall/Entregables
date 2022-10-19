#Imprimir info de la API

import time
import requests
import csv

for i in range(5):
 response=requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
 #Imprimir código de respuesta (si devuelve 200 está bien)
 #print(response.status_code)
 #Imprimir quote, character & image
 print(f'Quote {i+1}:')
 print(response.json()[0]["quote"])
 
 #Si el "character" es Homer te copia 'data' en el fichero Homer en la carpeta Homer
 if response.json()[0]["character"] == "Homer Simpson":
   with open('/Homer/Homer.csv', 'a') as Homer:
     data = [response.json()[0]["character"], response.json()[0]["quote"]]
     writer = csv.writer(Homer)
     writer.writerow(data)
 #Si el "character" es Lisa te copia 'data' en el fichero Lisa en la carpeta Lisa
 elif response.json()[0]["character"] == "Lisa Simpson":
   with open('/Lisa/Lisa.csv', 'a') as Lisa:
     data = [response.json()[0]["character"], response.json()[0]["quote"]]
     writer = csv.writer(Lisa)
     writer.writerow(data)
 #Si el "character" es otro te copia 'data' en el fichero General en la carpeta General
 else: 
   with open('/General/General.csv', 'a') as General:
     data = [response.json()[0]["character"], response.json()[0]["quote"]]
     writer = csv.writer(General)
     writer.writerow(data)
 
 print(" ")
 time.sleep(5)
