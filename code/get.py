import json

from pynamodb.exceptions import DoesNotExist
from agenda_model import AgendaModel


def get(event, context):
    try:
        found_todo = AgendaModel.get(hash_key=event['path']['user_id'])
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'TODO was not found'})}

    # create a response
    return {'statusCode': 200,
            'body': json.dumps(dict(found_todo))}

