import time
import requests
import csv
import os
from os import mkdir

for i in range(5):
  response = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
  print(f'image {i+1}:')
  char = response.json()[0]["character"]
  im = response.json()[0]["image"]
  quote = response.json()[0]["quote"]
  print(char)
  print (quote)
  print(im)
  
  lista = quote.split()
  for j in range(len(lista)):
    palabra = lista [j]
    print(f'{j+1} {palabra} \n')
    with open('/diccionario.csv', 'a') as diccionario:
      writer = csv.writer(diccionario)
      writer.writerow(f'{palabra} \n')

  url_imagen = (f'{im}') 
  imagen = requests.get(url_imagen).content

  nombre_local_imagen = (f'Imagen {i+1}_{char}')
  carpeta_personaje = os.path.exists(f'/{char}')
  if carpeta_personaje == False:
    os.mkdir (f'/{char}')

  with open(f'/{char}/{nombre_local_imagen}', 'wb') as character:
	      character.write(imagen) 
          
 time.sleep(5)