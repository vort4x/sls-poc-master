import json

from agenda_model import AgendaModel


def todo_list(event, context):
    # fetch all todos from the database
    results = AgendaModel.scan()

    # create a response
    return {'statusCode': 200,
            'body': json.dumps({'items': [dict(result) for result in results]})}
