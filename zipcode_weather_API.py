import requests
import json


def Temp_check():
    apiKey = 'afb8fda2b389d165dcd91d0b0a929ff2'
    while True:
        try:
            ville = input('Quel est votre code postal ?')
            # French Zip Code only
            url = 'http://api.openweathermap.org/data/2.5/weather?zip=' + ville + ',fr&appid='+ apiKey
            data = requests.get(url)
            data = data.json()
            temp = data['main']['temp']
            print(url)
            break
        except:
            print('Nom de ville non valide')
    current_weather = str(round((temp - 273.25), 1)) + '°C'
    return 'La température actuelle à {} est de {}'.format(data['name'], current_weather)

Temp_check()
    
    
