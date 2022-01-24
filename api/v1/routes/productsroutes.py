from fastapi import APIRouter
from api.v1.config.db import connection
from api.v1.models.productsmodel import Products
from api.v1.schemas.productsschema import productEntity, productsEntity

productsrouter = APIRouter()

@productsrouter.get('/{id}')
async def find_tags_by_productid(id):
    return productEntity(connection.local.products.find_one({"id": id}))

@productsrouter.get('/')
async def find_all_products_with_respective_tags():
    #print(connection.local.tags.find())
    #print(tagsEntity(connection.local.tags.find()))
    return productsEntity(connection.local.products.find())
    
@productsrouter.post('/')
async def create_product_with_respective_tags(tags: Products):
    connection.local.products.insert_one(dict(tags))
    return productsEntity(connection.local.products.find())

@productsrouter.put('/{id}')
async def update_product_and_or_tags(id, tags: Products):
    connection.local.products.find_one_and_update( {"id": id}, { "$set": dict(tags)})
    return productEntity(connection.local.products.find_one( {"id": id}))
    
@productsrouter.delete('/{id}')
async def delete_product_with_tags(id, tags: Products):
    return productEntity(connection.local.products.find_one_and_delete({"id": id}))