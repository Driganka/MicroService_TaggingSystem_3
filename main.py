from fastapi import FastAPI
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import JSONResponse

from api.v1.app import router as app_v1
from logger import create_logger

app = FastAPI(docs_url="/api/v1/docs", openapi_url="/api/v1/auth/openapi.json")
app.include_router(app_v1, prefix="/api/v1")

logging = create_logger(__name__)


@app.on_event("startup")
async def startup_event():
    logging.info("start up event")


#    await get_redis_pool()
#    mongo_conn = connect(
#         settings.database_name,
#         username=settings.db_username,
#         password=settings.db_password,
#         authentication_source=settings.authentication_source,
#         host=settings.host,
#         serverSelectionTimeoutMS=2000,
#     )


@app.on_event("shutdown")
async def shutdown_event():
    logging.info("shutdown event")


#    pool = await get_redis_pool()
#    pool.close()
#    await pool.wait_closed()
#    disconnect()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse({"Error": str(exc.detail)}, status_code=exc.status_code)
