from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from app.database import Base, engine
from app.models import User
from app.routers.auth import router as auth_router
from app.routers.dress import router as dress_router
from app.routers.measurement import router as measurement_router
from app.routers.order import router as order_router
from app.routers.admin import router as admin_router
from app.routers.dashboard import router as dashboard_router
from app.routers.upload import router as upload_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(dress_router)
app.include_router(measurement_router)
app.include_router(order_router)
app.include_router(admin_router)
app.include_router(dashboard_router)
app.include_router(upload_router)
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to TailorPro API"
    }