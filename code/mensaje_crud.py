import json
import logging
import uuid
from datetime import datetime
from pynamodb.exceptions import DoesNotExist

from mensaje_model import MensajeModel

def msg_get(event, context):
    try:
        found_todo = MensajeModel.get(hash_key=event['path']['mensaje_id'])
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'TODO was not found'})}

    # create a response
    return {'statusCode': 200,
            'body': json.dumps(dict(found_todo))}


def msg_list(event, context):
    results = MensajeModel.scan()

    return {'statusCode': 200,
            'body': json.dumps({'items': [dict(result) for result in results]})}

def msg_crear(event, context):
    data = json.loads(event['body'])

    a_todo = MensajeModel(mensaje_id=str(uuid.uuid1() ),
                       nombre=data['nombre'],
                       correo=data['correo'],
                       asunto=data['asunto'],
                       cuerpo=data['cuerpo'],
                       create_at = datetime.now())

    # write the todo to the database
    a_todo.save()

    # create a response
    return {'statusCode': 201,
            'body': json.dumps(dict(a_todo))}
            
