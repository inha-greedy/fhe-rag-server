from fastapi import APIRouter, Form, UploadFile

from ..services.enc import set_he_context
from ..services.key import save_key, load_public_key

key_router = APIRouter()


@key_router.post("/key")
async def set_encryption_key(file: UploadFile = Form(...)):

    # 1. byte -> file
    contents = await file.read()
    save_key(contents=contents)

    # 2. file -> HE (on memory)
    load_public_key()

    return "OK"
