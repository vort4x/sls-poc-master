import os
from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class MensajeModel(Model):
    
    class Meta:
        table_name = os.environ['DYNAMODB_MENSAJE']
        if 'ENV' in os.environ:
            host = 'http://localhost:8000'
        else:
            region = 'us-west-2'
            host = 'https://dynamodb.us-west-2.amazonaws.com'

    mensaje_id = UnicodeAttribute(hash_key=True, null=False)

    nombre = UnicodeAttribute(null=False)
    correo = UnicodeAttribute(null=False)
    asunto = UnicodeAttribute(null=False)
    cuerpo = UnicodeAttribute(null=False)
    

    leido = BooleanAttribute(null=False, default=False)

    create_at = UTCDateTimeAttribute(null=False, default=datetime.now())
    updated_at = UTCDateTimeAttribute(null=False)

    def save(self, conditional_operator=None, **expected_values):
        self.updated_at = datetime.now()
        super(MensajeModel, self).save()

    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))
