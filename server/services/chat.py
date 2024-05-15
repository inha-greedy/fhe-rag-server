from Pyfhel import Pyfhel, PyCtxt
from ..models.document import PyCDocument

from .enc import get_he_context
from .storage import get_content


def get_top_list(encrypted_query: PyCDocument):

    documents = get_content("documents")

    c_query_embedding = encrypted_query.embedding

    he = get_he_context()
    print(f"{he=}")

    for doc in documents:

        c_result = _compute_cosine_similarity(c_query_embedding, doc.embedding)

        computed_cosine_sim = decrypt_result(he, c_result)
        print(f"doc={doc.index}: {computed_cosine_sim}")

    return c_result


def decrypt_result(he: Pyfhel, c_result: PyCtxt) -> float:
    return he.decrypt(c_result)[0]


def _compute_cosine_similarity(ctxt_v1: PyCtxt, ctxt_v2: PyCtxt) -> PyCtxt:
    c_result = ctxt_v1 @ ctxt_v2
    return c_result
