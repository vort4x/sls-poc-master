import json

from pynamodb.exceptions import DoesNotExist
from agenda_model import AgendaModel

def buscar_auth(event, context):
    try:
        #data = json.loads(event['body'])
        out=[]
        

        results = AgendaModel.query(AgendaModel.paciente_id.startswith('p'))
        for user in results:
            out.append(user)
    except DoesNotExist:
        return {'statusCode': 404,
                'body': json.dumps({'error_message': 'TODO was not found'})}

    # create a response
    return {'statusCode': 200,
                'body': json.dumps(out)}

