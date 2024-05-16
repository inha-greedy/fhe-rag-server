from typing import List

from fastapi import APIRouter

from ..models.document import PyCDocumentDto
from ..services.storage import set_content

document_router = APIRouter()


@document_router.post("/enc-docs")
async def enc_docs(documents: List[PyCDocumentDto]):

    encrypted_documents = [doc.to_document() for doc in documents]

    set_content("encrypted_documents", encrypted_documents)
    # 처리된 문서 반환
    return "OK"
