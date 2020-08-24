import json
import logging
import uuid
from datetime import datetime
from pynamodb.exceptions import DoesNotExist

from usuario_model import UsuarioModel

def msg_get(event, context):
    try:
        found_todo = UsuarioModel.get(hash_key=event['path']['user_id'])
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'TODO was not found'})}

    # create a response
    return {'statusCode': 200,
            'body': json.dumps(dict(found_todo))}


def msg_list(event, context):
    results = UsuarioModel.scan()

    return {'statusCode': 200,
            'body': json.dumps({'items': [dict(result) for result in results]})}

def msg_crear(event, context):
    data = json.loads(event['body'])

    a_todo = UsuarioModel(user_id=data['user_id'],
                       nombre=data['nombre'],
                       correo=data['correo'],
                       password=data['password'],
                       rol=data['rol'],
                       create_at = datetime.now())


    # write the todo to the database
    a_todo.save()

    # create a response
    return {'statusCode': 201,
            'body': json.dumps(dict(a_todo))}
            

def msg_validausuario(event, context):
    data = json.loads(event['body'])
    resultado = "ok"
    found_todo = UsuarioModel.get(hash_key=data['user_id'])

    if data['password']==found_todo.password:
        resultado = "ok"
    else:
        resultado = "Password Incorreta"

    # create a response
    return {'statusCode': 200,
            'body': json.dumps(dict(resultado))}