import json
import utils
import requests
from datetime import datetime

def lambda_handler(event, context):
    
    # WEB HUBSPOT - VEHICULO
    
    data = json.loads(event["body"])

    # El número de días es la diferencia del último y penúltimo servicio
    # HubSpot envía la información en formato timestamp (milisegundos)
    # Se divide entre 86400000 para obtener los días

    numero_de_dias = float(data["properties"]["numero_de_dias"]["value"])/86400000
    
    # La fecha de servicio es el último servicio
    fecha_de_servicio = float(data["properties"]["fecha_de_servicio"]["value"])
    
    # El número de kilometraje es la diferencia del último y penúltimo kilometraje
    numero_de_km = float(data["properties"]["numero_de_km"]["value"])
    
    # Se obtiene valor de mantenimiento [5000, 10000, 15000, ...]
    valor_mantenimiento = float(data["properties"]["valor_de_mantenimiento"]["value"])  
    
    # Esta propiedad es la diferencia del valor de mantenimiento y el último kilometraje
    mantenimiento_X_km = float(data["properties"]["mantenimiento_x_km"]["value"])
    
    # El ID-registro del vehículo
    objectId = data["objectId"]
    
    # RATIO
    ratio = numero_de_km/numero_de_dias
    
    
    pronostico_dias = (mantenimiento_X_km/ratio)
    
    # Excepción solamente para el 2do mantenimiento
    if (valor_mantenimiento == 5000 and pronostico_dias > 150):
           
        pronostico_fecha = fecha_de_servicio + 150*86400000
            
    elif (pronostico_dias > 180):
        
        pronostico_fecha = fecha_de_servicio + 180*86400000
            
    else:
        pronostico_fecha = fecha_de_servicio + pronostico_dias*86400000
            
    
    dt_object = datetime.fromtimestamp(int(pronostico_fecha/1000))
    
    print("objectId:", objectId) 
    print("numero_de_km:", numero_de_km)
    print("numero_de_dias:", numero_de_dias)
    print("ratio:", ratio)
    print("mantenimiento_X_km:", mantenimiento_X_km)
    print("valor_mantenimiento:", valor_mantenimiento)
    print("pronostico_fecha:", pronostico_fecha)
    print("pronostico_dias:", pronostico_dias)
    print("fecha ", dt_object)
  
    try:
        respuesta = utils.update_vehiculo(objectId, dt_object.date(), pronostico_dias)
        return {
            'statusCode': 200,
            'body': respuesta
        }
    except ValueError:
        return {
            'statusCode': 502
            
        }
    

    
