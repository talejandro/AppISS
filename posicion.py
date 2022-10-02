from configparser import MAX_INTERPOLATION_DEPTH
from urllib.request import urlopen
import json
import time

url = 'https://api.wheretheiss.at/v1/satellites/25544'

loops = 2

while loops != 1: 
    req = urlopen(url)
    response = req
    data = json.loads(response.read())
    position_iss = {
                "Tiempo" : data['timestamp'],
                "Latitud" : data['latitude'], 
                "Longitud" : data['longitude'], 
                "Velocidad" : data['velocity']}
    with open('iss.json', 'w') as f:  
        json.dump(position_iss, f)
    time.sleep(5)