from typing import List

from fastapi import APIRouter, Request
import numpy as np

from ..models.document import PyCDocumentDto
from ..services.chat import get_top_list

chat_router = APIRouter()


@chat_router.post("/emb-query")
async def upload_emb_query(documents: List[PyCDocumentDto]):

    encrypted_query = documents[0].to_document()

    top_list = get_top_list(encrypted_query=encrypted_query)

    print(f"{encrypted_query=}")

    return "OK"
