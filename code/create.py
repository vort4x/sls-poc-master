import json
import logging
import uuid
from datetime import datetime

from agenda_model import AgendaModel


def create(event, context):
    data = json.loads(event['body'])

    if 'paciente_id' not in data:
        logging.error('Validation Failed')
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the todo item.'})}

    if not data['paciente_id']:
        logging.error('Validation Failed - text was empty. %s', data)
        return {'statusCode': 422,
                'body': json.dumps({'error_message': 'Couldn\'t create the todo item. As text was empty.'})}

    agenda_id = data['fecha_evento']+"_"+data['paciente_id']
    a_todo = AgendaModel(agenda_id=agenda_id,
                       paciente_id=data['paciente_id'],
                       tipo_evento=data['tipo_evento'],
                       fecha_evento=data['fecha_evento'],
                       create_at = datetime.now())

    # write the todo to the database
    a_todo.save()

    # create a response
    return {'statusCode': 201,
            'body': json.dumps(dict(a_todo))}
            
