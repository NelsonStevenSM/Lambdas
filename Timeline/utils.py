import os
import requests
import json
def create_event(email, date_hour, nombreDelNegocio):
    # Obtener el token oauth
    
    get_tokens = "https://api.hubapi.com/oauth/v1/token"
    
    headers_tokens = {
        'content-type': "application/x-www-form-urlencoded"
    }
    
    payload_tokens = 'refresh_token=ce0a210c-c2fe-4db4-bcb7-0be1e8aab0e2&grant_type=refresh_token&client_id=03653894-ac9a-48c5-ac2d-d0f001aba4c2&client_secret=68d4d76f-9bb1-4815-9d50-604897ed363c'
    
    response = requests.request("POST", get_tokens, data=payload_tokens, headers=headers_tokens)
    
    get_tokens_refresh = json.loads(response.text)["access_token"]
    print(get_tokens_refresh)
    # Creando un evento del timeline en el objeto contacto
    
    url = "https://api.hubapi.com/crm/v3/timeline/events"
    
    payload = "{\"eventTemplateId\": \"1079945\",\"email\":\""+ str(email)+"\",\"tokens\":{\"ActividadNegocio\":\""+ str(int(date_hour)) +"\",\"nombreDelNegocio\":\""+ str(nombreDelNegocio) +"\"}}"
    
    headers = {
        'authorization':"Bearer " + get_tokens_refresh,
        'accept': "application/json",
        'content-type': "application/json"
        }
    
    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
    
    return response.text

