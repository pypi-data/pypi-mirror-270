#Imports necesarios para las funciones de la libreria
import requests
from fastapi.responses import JSONResponse

#Metodo de prueba para el despliege de la libreria
def hola_journey():
    print('Holitaa, esta es una librería diseñada y publicada por JourneyGen.')



#Implementacion de las funciones necesarias para la libreria
endpoint = 'http://ismi.fi.upm.es:8080/endpoint'
"""
METODO INSERTAR HISTORICO
Descripcion: Inserta un nuevo par de mensajes a la bd de CASH
"""
def ins_historico(usr, num_chat, lista_msg, url=endpoint):
    
    datos_post = { # Formato con el que se consume la api
        'id_usuario': usr,
        'num_chat': num_chat,
        'msg': lista_msg
    }
    response = requests.post(url, json=datos_post)

    return JSONResponse(content=response.json(), status_code=response.status_code)