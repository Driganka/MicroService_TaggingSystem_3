from datetime import datetime

from mongoengine import DateTimeField, DynamicDocument, StringField


## A separate order detail because we want to encrypts
class Tags(DynamicDocument):
    name = StringField(required=True)
    service = StringField()
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
