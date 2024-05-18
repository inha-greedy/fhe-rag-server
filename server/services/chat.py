import base64

from typing import List

from Pyfhel import PyCtxt

from ..models.document import PyCDocumentDto
from ..models.similarity import PyCSimilarityDto
from .storage import load_documents


def get_similarities(query_embedding: PyCtxt) -> List[PyCSimilarityDto]:
    documents = load_documents()

    encrypted_similarities = []

    for doc in documents:
        enc_score = _compute_cosine_similarity(query_embedding, doc.embedding)

        encrypted_similarity = PyCSimilarityDto(
            index=doc.index,
            score=base64.b64encode(enc_score.to_bytes()).decode("utf-8"),
        )
        encrypted_similarities.append(encrypted_similarity)

    return encrypted_similarities


def get_documents_from_indices(indices: List[int]) -> List[PyCDocumentDto]:
    documents = load_documents()

    matched_documents: List[PyCDocumentDto] = []

    for index in indices:
        for doc in documents:
            if doc.index == index:
                matched_documents.append(
                    PyCDocumentDto(
                        index=doc.index,
                        document=base64.b64encode(doc.document.to_bytes()).decode("utf-8"),
                        embedding=base64.b64encode(doc.embedding.to_bytes()).decode("utf-8"),
                    )
                )

                continue

    return matched_documents


def _compute_cosine_similarity(ctxt_v1: PyCtxt, ctxt_v2: PyCtxt) -> PyCtxt:
    return ctxt_v1 @ ctxt_v2
