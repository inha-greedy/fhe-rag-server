from typing import List

from fastapi import APIRouter

from ..models.document import PyCDocumentDto
from ..services.storage import save_documents


document_router = APIRouter()


@document_router.post("/upload-docs")
async def upload_documents(documents: List[PyCDocumentDto]):
    save_documents(documents=documents)

    return "OK"
