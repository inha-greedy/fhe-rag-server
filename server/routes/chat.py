from typing import List

from fastapi import APIRouter

from ..models.document import PyCDocumentDto
from ..models.similarity import PyCSimilarityDto
from ..services.chat import get_documents_from_indices, get_similarities
from ..services.storage import load_he_from_key

chat_router = APIRouter()


@chat_router.post("/get-similarities")
async def get_similarities_from_query(documents: List[PyCDocumentDto]) -> List[PyCSimilarityDto]:
    he = load_he_from_key()
    query_document = documents[0].to_document(he=he)
    query_embedding = query_document.embedding

    similarities = get_similarities(query_embedding=query_embedding)

    return similarities


@chat_router.post("/get-docs")
async def get_docs_from_indices(
    indices: List[int],
) -> List[PyCDocumentDto]:
    documents = get_documents_from_indices(indices=indices)

    # 처리한 문서 반환
    return documents
