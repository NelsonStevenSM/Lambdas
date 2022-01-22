
import os
import requests


def update_vehiculo(objectId, pronostico_fecha, pronostico_dias):
    url = "https://api.hubapi.com/crm/v3/objects/2-2316394/" + str(objectId)
    hapikey = os.environ['API_KEY']
    querystring = {"hapikey": str(hapikey)}
    payload = "{\"properties\":{\"pronostico_fecha\":\""+ str(pronostico_fecha) + "\",\"pronostico_dias\":\""+ str(pronostico_dias)+"\"}}"
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    
    response = requests.request("PATCH", url, data=payload, headers=headers, params=querystring)
    
    print(response)
    return response.text

        
