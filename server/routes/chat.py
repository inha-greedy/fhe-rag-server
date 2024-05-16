from typing import List

from fastapi import APIRouter

from ..models.document import PyCDocumentDto
from ..services.chat import get_top_list

chat_router = APIRouter()


@chat_router.post("/emb-query")
async def upload_emb_query(documents: List[PyCDocumentDto]):

    c_query_document = documents[0].to_document()

    top_list = get_top_list(c_query_document=c_query_document)

    print(f"{c_query_document=}")

    return top_list
