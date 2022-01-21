
import os
import requests


def get_data_campana(version, model_year, fabrication_year):
    url = "https://api.hubapi.com/crm/v3/objects/2-2523016/search"
    hapikey = os.environ['API_KEY']
    querystring = {"hapikey": str(hapikey)}
    payload = "{\"filterGroups\":[{\"filters\":[{\"value\":\""+ version +"\",\"propertyName\":\"vehiculo\",\"operator\":\"EQ\"},{\"value\":\""+ fabrication_year +"\",\"propertyName\":\"ano_de_fabricacion\",\"operator\":\"EQ\"},{\"value\":\""+ model_year +"\",\"propertyName\":\"ano_de_modelo\",\"operator\":\"EQ\"}]}],\"sorts\":[\" \"],\"query\":\" \",\"properties\":[\"precio____\",\"color\",\"name_camp\",\"ano_campana\",\"mes_campana\"],\"limit\":10,\"after\":0}"
    headers = {
        'accept': "application/json",
        'content-type': "application/json"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    
    campana = set()
    color = set()
    precio = set()

    for i in response.json()["results"]:
        campana.add(i["properties"]["name_camp"])
        color.add(i["properties"]["color"])
        precio.add(i["properties"]["precio____"])

    data = [", ".join(list(campana)),", ".join(list(color)),", ".join(list(precio))]
    return data

