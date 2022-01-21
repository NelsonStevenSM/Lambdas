#Esta es la version que se usa en las pruebas
import json

def lambda_handler(event, context):
    # TODO implement
    dealname = event["multiValueQueryStringParameters"]["dealname"][0]
    id_negocio = event["multiValueQueryStringParameters"]["associatedObjectId"][0]
    
    datos_faltante = []
    
    try: 
        id_mrs = event["multiValueQueryStringParameters"]["hubspot_owner_id"][0]
        if (id_mrs == ""):
            datos_faltante.append("Falta Propietario del Negocio")
    except:
        datos_faltante.append("Falta Propietario del Negocio")
        
    
        
    
    try:
        procedencia = event["multiValueQueryStringParameters"]["procedencia_del_documento"][0]
        
        if(procedencia!="V" and procedencia!="S"):
            error = "La procedencia del documento es solo valida para Vehiculo o Servicio"
            if (procedencia == ""):
                error = "Falta el campo Procedencia"
            datos_faltante.append(error)
        
        if(procedencia=="V"):
            procedencia="Vehículo"
        if(procedencia=="S"):
            procedencia="Servicio"
        
    except:
        datos_faltante.append("Falta el campo Procedencia")
        
    
        
    if (len(datos_faltante)>0):
        datos_faltante_string = " || ".join(datos_faltante)
        return {
        'statusCode': 200,
        'body': json.dumps({
        "results": [
            {
                #'data' : event,
                "objectId": 123,
                "title": "Información de la cita",
                #"link": "https://gclientes.toyotaperu.com.pe/cotizador/Login.action",
                "description": "Esta es la primera prueba de la app con crm cards, se muestra en todos.",
                "properties": [
                    {
                    "label": "Error",
                    "dataType": "STRING",
                    "value":  datos_faltante_string
                    }
                ],
                #"actions": [
                #{
                #  "type": "IFRAME",
                #  "width": 1800,
                #  "height": 700,
                #  "uri": "https://gclientes.toyotaperu.com.pe/cotizador/",
                #  "label": "SGC",
                #  "associatedObjectProperties": []
                #}],
                
            }
        
      ]
     
    })
    }
        
    try:
        modelo = event["multiValueQueryStringParameters"]["vehiculo_modelo"][0]
    except:
        modelo = "-"
    try:
        placa = event["multiValueQueryStringParameters"]["placa"][0]
    except:
        placa = "-"
    
    
    
    

    return {
        'statusCode': 200,
        'body': json.dumps({
        "results": [
            {
                #'data' : event,
                "objectId": 123,
                #"link": "https://gclientes.toyotaperu.com.pe/cotizador/Login.action",
                "title": "Información de la cita",
                "description": "Esta es la primera prueba de la app con crm cards, se muestra en todos.",
                "properties": [
                    {
                    "label": "Nombre del Negocio",
                    "dataType": "STRING",
                    "value":  dealname
                    },
                    {
                    "label": "Modelo del vehiculo",
                    "dataType": "STRING",
                    "value":  modelo
                    },
                    {
                    "label": "Placa",
                    "dataType": "STRING",
                    "value":  placa
                    },
                    {
                    "label": "Prodecendia",
                    "dataType": "STRING",
                    "value":  procedencia
                    },
                    {
                    "label": "ID del MRS",
                    "dataType": "STRING",
                    "value": id_mrs
                    },
                    {
                    "label": "ID del negocio",
                    "dataType": "STRING",
                    "value":  id_negocio
                    },
                ],
                #"actions": [
                #{
                #  "type": "IFRAME",
                #  "width": 1800,
                #  "height": 700,
                #  "uri": "https://gclientes.toyotaperu.com.pe/cotizador/Login.action",
                #  "label": "SGC"
                #}],
                #"actions": [
                #{
                #  "type": "IFRAME",
                #  "width": 2000,
                #  "height": 950,
                #   #"uri": "https://webcitas.azurewebsites.net/?idNegocio=5898932338&procedencia=V&owner=79870886&negocio=demo&modelo=ETIOS&placa=AWX987",
                #  "uri": "https://panacitas.azurewebsites.net/",
                #  #"uri": "https://webhook.site/a79dbc40-1f31-4dea-8422-ed6471a82108",
                #  "label": "WebCitas",
                #  "associatedObjectProperties": [
                #    "associatedObjectId",
                #    "hs_object_id",
                #    "procedencia_del_documento",
                #    "hubspot_owner_id",
                #    "dealname",
                #    "vehiculo_modelo",
                #    "placa"
                #  ]
                #  
                #},
                #]
                    
            }
        
        ], 
        "primaryAction": {
        "type": "IFRAME",
        "width": 2000,
        "height": 950,
        "uri": "https://panacitas.azurewebsites.net/",
        "label": "Abrir WebCitas",
        "associatedObjectProperties": [
            "associatedObjectId",
            "hs_object_id",
            "procedencia_del_documento",
            "hubspot_owner_id",
            "dealname",
            "vehiculo_modelo",
            "placa"
          ]
        }
    })
    }

    



