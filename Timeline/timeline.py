import json
import requests
import utils
import datetime
import datetime

def lambda_handler(event, context):
    
    body = event["body"]
    
    data = json.loads(body)
    
    property_email = data["properties"]["email"]["value"]
    nombre_del_Negocio = data["properties"]["nombre_del_negocio_registrado"]["value"]
    min5 = datetime.timezone(datetime.timedelta(hours=-5))

    date_hour = datetime.datetime.now(min5)
    #format_date_hour = date_hour.strftime("%x") + " " + date_hour.strftime("%X")
    format_date_hour = datetime.datetime.timestamp(date_hour)*1000
    
    #print(datetime.datetime.timestamp(date_hour)*1000)
    print(format_date_hour)
    print(nombre_del_Negocio)

    return {
        'statusCode': 200,
        'body': json.dumps(utils.create_event(property_email, format_date_hour, nombre_del_Negocio))
    }
    
    
    
