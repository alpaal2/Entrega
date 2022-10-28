import time
import requests
import pandas as pd

while True: 
    time.sleep(30)
    URL = 'https://thesimpsonsquoteapi.glitch.me/quotes'
    respuesta = requests.get (URL)
    datos = respuesta.json()
    frasesimpson = datos[0]['quote']
    personajesimpson = datos [0]['character']
    print(f'La frase de {personajesimpson} es: {frasesimpson}')
    if 'Homer Simpson' in personajesimpson:
       frasehomer = {f'{personajesimpson}',f'{frasesimpson}'}
       da=pd.DataFrame(frasehomer)
       da.to_csv('C:\\Users\\PALANCA\\Desktop\\EDEM\\Simpsons\\Homer\\homer.csv', mode='a', header=True, index=False)
    elif 'Lisa Simpson' in personajesimpson:
       fraselisa = {f'{personajesimpson}',f'{frasesimpson}'}
       de=pd.DataFrame(fraselisa)
       de.to_csv('C:\\Users\\PALANCA\\Desktop\\EDEM\\Simpsons\\Lisa\\lisa.csv', mode='a', header=True, index=False)
    else: 
       frasegen = {f'{personajesimpson}',f'{frasesimpson}'}
       df=pd.DataFrame(frasegen)
       df.to_csv('C:\\Users\\PALANCA\\Desktop\\EDEM\\Simpsons\\General\\general.csv', mode='a', header=True, index=False)