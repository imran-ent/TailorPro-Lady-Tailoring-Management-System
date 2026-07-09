import os
import shutil
from uuid import uuid4

from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/")
def upload_image(
    file: UploadFile = File(...)
):

    extension = file.filename.split(".")[-1]

    filename = f"{uuid4()}.{extension}"

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename,
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer,
        )

    return {
        "filename": filename,
        "path": filepath,
    }