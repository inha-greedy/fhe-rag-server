from fastapi import APIRouter, Form, UploadFile

from ..services.storage import save_public_key


key_router = APIRouter()


@key_router.post("/sync-key")
async def sync_key(file: UploadFile = Form(...)):
    # byte -> file
    contents = await file.read()
    save_public_key(contents=contents)

    return "OK"
