from fastapi import FastAPI
from api.v1.routes.tagsroutes import tagsrouter
from api.v1.routes.productsroutes import productsrouter

app = FastAPI()

#app.include_router(tagsrouter)

app.include_router(tagsrouter, prefix="/users", tags=["USERS WITH TAGS"])
app.include_router(productsrouter, prefix="/products", tags=["PRODUCTS WITH TAGS"])
