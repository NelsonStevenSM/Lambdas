import json
import utils
import requests
from datetime import datetime
import utils
import ast

def lambda_handler(event, context):

    #url = "https://webhook.site/bc1df61b-3485-45a2-8d07-5696ff8206d2"
    #data = requests.post(url, data={"Hs": json.dumps(event)})
    #print(data.json)
    
    associatedObjectId = event["queryStringParameters"]["associatedObjectId"]
    idContact = utils.get_Id_Contact(associatedObjectId)
    
    pipeline = utils.get_all_pipeline()
    list_deals = utils.get_all_deals(idContact)
    pipe_stages = utils.get_pipe_and_stage_deals(list_deals)
   
    ID_PIPE_TITLE = {
        261120210 : ["14992112", "PRE-VENTA DE SERVICIO"],
        261120211 : ["default", "VENTA DE SERVICIO"],
        261120212 : ["990098", "PRE-VENTA DE VEHÍCULO"],
        261120213 : ["990043", "VENTA DE VEHÍCULO"],
    }
    
    temp = {"results":[]}
    
    for objectId, id_name_pipeline in ID_PIPE_TITLE.items():
        count = 0
        array_temp = {
            "objectId": objectId,
            "title": id_name_pipeline[1],
            "description": "Esta es la primera prueba de la app con crm cards, se muestra en todos.",
            "properties": [],
            }
        
        for deals, (k, v) in zip(list_deals, pipe_stages.items()):
            temp_gp = {}
            if (v[0] == id_name_pipeline[0]):
                count += 1
                if (deals.get("id") != associatedObjectId):
                    temp_gp = {
                        "label": "-",
                        "dataType": "LINK",
                        "value": "https://app.hubspot.com/contacts/8459312/deal/"+ str(k),
                        "linkLabel": v[2] + " / " + pipeline.get(v[1])
                    }
                else:
                    temp_gp = {
                        "label": "-",
                        "dataType": "STRING",
                        "value": v[2] + " / " + pipeline.get(v[1])
                    }
                    
            if (temp_gp != {}):
                array_temp["properties"].append(temp_gp)   
            
        array_temp["title"] += " ( {} )".format(str(count))
        temp["results"].append(array_temp)
        

    print(json.dumps(temp))

    return {
        'statusCode': 200,
        'body': json.dumps(temp)
    }    
        
