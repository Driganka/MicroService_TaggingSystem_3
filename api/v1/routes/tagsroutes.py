from fastapi import APIRouter
from api.v1.config.db import connection
from api.v1.models.tagsmodel import Tags
from api.v1.schemas.tagsschema import tagEntity, tagsEntity

tagsrouter = APIRouter()

@tagsrouter.get('/{id}')
async def find_tags_by_userid(id):
    return tagEntity(connection.local.tags.find_one({"id": id}))

@tagsrouter.get('/')
async def find_all_users_with_respective_tags():
    #print(connection.local.tags.find())
    #print(tagsEntity(connection.local.tags.find()))
    return tagsEntity(connection.local.tags.find())
    
@tagsrouter.post('/')
async def create_user_with_respective_tags(tags: Tags):
    connection.local.tags.insert_one(dict(tags))
    return tagsEntity(connection.local.tags.find())

@tagsrouter.put('/{id}')
async def update_user_and_or_tags(id, tags: Tags):
    connection.local.tags.find_one_and_update( {"id": id}, { "$set": dict(tags)})
    return tagEntity(connection.local.tags.find_one( {"id": id}))
    
@tagsrouter.delete('/{id}')
async def delete_user_with_tags(id, tags: Tags):
    return tagEntity(connection.local.tags.find_one_and_delete({"id": id}))