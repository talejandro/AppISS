from operator import is_
import requests
from datetime import datetime
import time
import json

Mi_Latitud = 50.2008
Mi_Longitud = 158.4937

#funcion para determinar si esta en el campo de vision del usuario
def iss_campo_vision():

    with open('iss.json') as jfile:  
        datos = json.load(jfile)
        iss_latitud = float(datos['Latitud'])
        iss_longitud = float(datos['Longitud'])

    #Si la posicion del usuario esta +- 5grados, la iss esta visible

    if Mi_Latitud - 5 <= iss_latitud <= Mi_Latitud + 5 and Mi_Longitud -5 <= iss_longitud <= Mi_Longitud + 5 :
        return True

       

def iss_noche():

    datos_usr = {
        "lat": Mi_Latitud,
        "lng": Mi_Longitud,
        "formatted": 0,
    }

    comprobar = requests.get("https://api.sunrise-sunset.org/json", params=datos_usr)
    comprobar.raise_for_status()
    data = comprobar.json()
    
    amanecer = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    anochecer = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    #if time_now >= anochecer or time_now <= amanecer:
     #   return True
    return True


def iss_visible():
    if iss_campo_vision() and iss_noche():
        print('La iss es visible!')
    else:
        print('No es visible :c')


iss_visible()