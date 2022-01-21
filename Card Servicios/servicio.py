import json
import utils
import requests
from datetime import datetime
import utils
import ast

def lambda_handler(event, context):
    # Se obtiene el dealId del negocio
    associatedObjectId = event["queryStringParameters"]["associatedObjectId"]
    
    # Se obtiene el Id de la asociación
    idContact = utils.get_Id_Contact(associatedObjectId)
    
    # Se mostrará un mensaje de información cuando el negocio no tiene asociado a un contacto
    if idContact == 400:
        return {
            'statusCode': 200,
            'body': json.dumps({
                "results": [{
                        "objectId": 123,
                        "title": "Información",
                        "properties": [{
                            "label": "Error",
                            "dataType": "STRING",
                            "value":  "No está asociado a un contacto"
                        }]
                    }]
            })
        }
        
    # Se obtiene todos los pipeline de la cuenta para luego filtrarlo con el dealid 
    # según la etapa de los demás negocios
    pipeline = utils.get_all_pipeline()
    
    # Se obtiene todos los negocios que están asociados al contacto
    list_deals = utils.get_all_deals(idContact)
    
    # Se filtra según el pipeline y la etapa del negocio de cada negocio
    pipe_stages = utils.get_pipe_and_stage_deals(list_deals)
    
    # objectId: [Id del pipeline, Nombre del pipeline]
    ID_PIPE_TITLE = {
        261120212 : ["16647267", "Pre-venta de servicios"],
        261120213 : ["16586522", "Venta de servicios"]
    }
    
    # Contruir el resultado para que se muestre en las tarjetas personalizadas.
    temp = {"results":[]}
    
    for objectId, id_name_pipeline in ID_PIPE_TITLE.items():
        count = 0
        array_temp = {
            "objectId": objectId,
            "title": id_name_pipeline[1],
            "description": "Esta es la primera prueba de la app con crm cards, se muestra en todos.",
            "properties": [],
            }
        
        for k, v in pipe_stages.items():
            # k = Es el Id del negocio asoaciado al contacto
            # v = Nombre del negocio y su etapa de negocio
            temp_gp = {}
            
            if (v[0] == id_name_pipeline[0]):
                count += 1
                
                if (str(k) != associatedObjectId):
                    # Los negocios asociados al contacto tendrán una URL
                    temp_gp = {
                        "label": ":",
                        "dataType": "LINK",
                        "value": "https://app.hubspot.com/contacts/9480697/deal/"+ str(k),
                        "linkLabel": v[2] + " / " + pipeline.get(v[1])
                    }
                    
                else:
                    # Es el negocio que hace la solicitud para mostrar los demás negocios (se omite el URL)
                    temp_gp = {
                        "label": "-",
                        "dataType": "STRING",
                        "value": v[2] + " / " + pipeline.get(v[1])
                    }
            
            
            if (temp_gp != {}):
                array_temp["properties"].append(temp_gp)
                
        # Se configura la cantidad de negocios que se encuentran en cada pipeline
        array_temp["title"] += " ( {} )".format(str(count))
        temp["results"].append(array_temp)
        

    print(json.dumps(temp))

    return {
        'statusCode': 200,
        'body': json.dumps(temp)
    }    
        
   
    
