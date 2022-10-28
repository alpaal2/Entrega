import requests
import os
import time

while True: 
    time.sleep(5)
    URL = 'https://thesimpsonsquoteapi.glitch.me/quotes'
    respuesta = requests.get (URL)
    datos = respuesta.json()
    URL_imagen = datos[0]['image']
    imagen = requests.get(URL_imagen).content
    nombre_imagen = "personaje.png"
    personajesimpson = datos [0]['character']

    with open (nombre_imagen, 'wb') as handler:
      handler.write(imagen)
