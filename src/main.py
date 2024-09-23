import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import ORJSONResponse
from contextlib import asynccontextmanager

from starlette.middleware.errors import ServerErrorMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from src.core import config

from src.api.v1 import recognition
from middleware import LoggingMiddleware, BeforeRequest

settings = config.get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """@app.on_event("startup") and @app.on_event("shutdown") was deprecated.\n
    Recommended to use "lifespan"."""
    # start_up
    #pass
    #await init_models()
    yield
    #await purge_pg_database()


app = FastAPI(
    title=settings.project_name,
    description='Сервис распознавания изображений',
    version='1.0',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
    #dependencies=[Depends(security_jwt(required_roles=[]))]
)


#app.add_middleware(BeforeRequest)
app.add_middleware(LoggingMiddleware)
app.add_middleware(ServerErrorMiddleware)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])


app.include_router(recognition.router, prefix='/api/v1/recognition', tags=['recognition'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.app_host,
        port=settings.app_port,
    )
