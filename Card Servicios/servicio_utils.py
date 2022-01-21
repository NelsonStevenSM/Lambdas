import os
import requests
import json

def get_Id_Contact(associatedObjectId):
    
    url = "https://api.hubapi.com/crm/v3/associations/0-3/0-1/batch/read"
    
    hapikey = os.environ['API_KEY']
    
    querystring = {"hapikey": str(hapikey)}
    
    payload = "{\"inputs\":[{\"id\":\""+ associatedObjectId + "\"}]}"
    
    headers = {
        'content-type': "application/json"
        }
        
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    
    if len(response.json()["results"]) != 0:
        return response.json()["results"][0]["to"][0]["id"]
    else:
        return 400
    
    
def get_all_pipeline():
    
    url = "https://api.hubapi.com/crm/v3/pipelines/0-3?archived=false"
    
    hapikey = os.environ['API_KEY']
    
    querystring = {"hapikey": str(hapikey)}
    
    headers = {
        'content-type': "application/json"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    pipeline = response.json()["results"]

    id_label_pipe = {}
    
    for pipe in pipeline:
        id_label_pipe[pipe.get("id")] = pipe.get("label")
        
        for stages in pipe.get("stages"):
            id_label_pipe[stages.get("id")] = stages.get("label")
            
        continue

    return id_label_pipe
    
    
def get_all_deals(idContact):
    
    url = "https://api.hubapi.com/crm/v3/objects/contacts/" + idContact + "/associations/0-3?limit=500"
    
    hapikey = os.environ['API_KEY']
    
    querystring = {"hapikey": str(hapikey)}
    
    headers = {
        'content-type': "application/json"
        }
        
    response = requests.request("GET", url, headers=headers, params=querystring)

    return [{"id" : id_deal.get("id")} for id_deal in response.json()["results"]]
    
def get_pipe_and_stage_deals(list_deals):
    
    url = "https://api.hubapi.com/crm/v3/objects/deals/batch/read?archived=false"
    
    hapikey = os.environ['API_KEY']
    
    querystring = {"hapikey": str(hapikey)}
    
    payload = "{\"properties\":[\"pipeline\", \"dealstage\", \"dealname\"],\"inputs\":"+ json.dumps(list_deals) +"}"

    
    headers = {
        'content-type': "application/json"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    return {result["properties"].get("hs_object_id") : [result["properties"].get("pipeline"), result["properties"].get("dealstage"), result["properties"].get("dealname")] for result in response.json()["results"]}
