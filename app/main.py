from fastapi import FastAPI
from app.routers.core.healthcheck import healthcheck_router


app = FastAPI(title="test-weaviate")
app.include_router(healthcheck_router)