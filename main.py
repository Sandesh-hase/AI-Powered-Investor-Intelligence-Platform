from fastapi import FastAPI

from routes.dashboard import router as dashboard_router
from routes.chat import router as chat_router
from routes.health import router as health_router
from routes.ingestion import router as ingestion_router

app = FastAPI(
    title="FinSight AI",
    version="1.0.0"
)

app.include_router(
    health_router,
    tags=["Health"]
)

app.include_router(
    ingestion_router,
    prefix="/api",
    tags=["Ingestion"]
)

app.include_router(
    dashboard_router,
    prefix="/api",
    tags=["Dashboard"]
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
