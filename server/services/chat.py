from typing import List

from Pyfhel import Pyfhel, PyCtxt
from ..models.document import PyCDocument
from ..models.similarity import PyCSimilarity, Similarity


from .enc import get_he_context
from .storage import get_content


def get_top_list(c_query_document: PyCDocument) -> List[PyCSimilarity]:

    encrypted_documents = get_content("encrypted_documents")

    he = get_he_context()

    c_similarity_list = []

    sim_list = []  # debug

    for doc in encrypted_documents:

        c_score = _compute_cosine_similarity(c_query_document.embedding, doc.embedding)

        similarity = PyCSimilarity(index=doc.index, score=c_score)
        c_similarity_list.append(similarity)

        # debug
        score = decrypt_result(he, c_score)
        print(f"{score=}")
        sim_list.append(Similarity(index=doc.index, score=score[0]))

    print(sim_list)  # debug
    return sim_list

    return c_similarity_list


def decrypt_result(he: Pyfhel, c_result: PyCtxt) -> float:
    return he.decrypt(c_result)


def _compute_cosine_similarity(ctxt_v1: PyCtxt, ctxt_v2: PyCtxt) -> PyCtxt:
    c_result = ctxt_v1 @ ctxt_v2
    return c_result
