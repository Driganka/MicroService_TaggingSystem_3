from fastapi import FastAPI
from api.v1.routes.tagsroutes import tagsrouter

app = FastAPI()

#app.include_router(tagsrouter)

app.include_router(tagsrouter, prefix="/users", tags=["USERS WITH TAGS"])