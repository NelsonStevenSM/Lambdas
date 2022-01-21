
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

 associatedObjectId = event["queryStringParameters"]["associatedObjectId"]
    idContact = utils.get_Id_Contact(associatedObjectId)
    
    pipeline = utils.get_all_pipeline()
    list_deals = utils.get_all_deals(idContact)

    pipe_stages = utils.get_pipe_and_stage_deals(list_deals)
    print(".---------------------")
    print(pipe_stages)
   
    id_pipe_title = {
        261120210 : ["14992112", "PRE VENTA DE SERVICIO"],
        261120211 : ["default", "VENTA DE SERVICIO"],
        261120212 : ["990098", "VENTA DE VEHÍCULO"]
    }
    temp = {"results":[]}
    
    for objectId, id_name_pipeline in id_pipe_title.items():
        
    
        array_temp = {
            "objectId": objectId,
            "title": id_name_pipeline[1],
            "description": "Esta es la primera prueba de la app con crm cards, se muestra en todos.",
            "properties": [],
            }
        
        temp_gp = {}
        for deals, (k, v) in zip(list_deals, pipe_stages.items()):
            if (k == id_name_pipeline[0]):
                
                if (deals.get("id") != associatedObjectId):
                    temp_gp = {
                        "label": "-",
                        "dataType": "LINK",
                        "value": "https://app.hubspot.com/contacts/8459312/deal/"+ str(deals.get("id")),
                        "linkLabel": v[1] + " / " + pipeline.get(v[0])
                    }
                else:
                    temp_gp = {
                        "label": "-",
                        "dataType": "STRING",
                        "value": v[1] + " / " + pipeline.get(v[0])
                    }
                    
            if (temp_gp != {}):
                array_temp["properties"].append(temp_gp)   
            temp_gp = {}
        temp["results"].append(array_temp)

    print(json.dumps(temp))

    return {
        'statusCode': 200,
        'body': json.dumps(temp)
    }    
        
