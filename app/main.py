from fastapi import FastAPI

from app.database import Base, engine
from app.models import User
from app.routers.auth import router as auth_router
from app.routers.dress import router as dress_router
from app.routers.measurement import router as measurement_router
from app.routers.order import router as order_router
from app.routers.admin import router as admin_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(dress_router)
app.include_router(measurement_router)
app.include_router(order_router)
app.include_router(admin_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to TailorPro API"
    }