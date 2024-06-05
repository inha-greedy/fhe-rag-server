import os
import zipfile
import json
from typing import List

from Pyfhel import Pyfhel

from ..models.document import PyCDocumentDto, PyCDocument
from .session import get_user_id


def save_documents(documents: List[PyCDocumentDto]) -> None:
    document_path = _get_document_path()

    data = [doc.model_dump() for doc in documents]

    with open(document_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_documents() -> List[PyCDocument]:
    document_path = _get_document_path()

    try:
        with open(document_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    he = load_he_from_key()
    documents = [PyCDocumentDto(**doc).to_document(he=he) for doc in data]

    return documents


def save_public_key(contents: bytes) -> None:
    key_path = _get_key_path()

    with open(key_path, "wb") as fp:
        fp.write(contents)

    print(f"key saved: {key_path}")


def load_he_from_key() -> Pyfhel:
    key_path = _get_key_path()

    he = Pyfhel()

    with zipfile.ZipFile(key_path, "r") as zipf:
        with zipf.open("context.bytes") as f:
            he.from_bytes_context(f.read())
        with zipf.open("public_key.bytes") as f:
            he.from_bytes_public_key(f.read())
        with zipf.open("relin_key.bytes") as f:
            he.from_bytes_relin_key(f.read())
        with zipf.open("rotate_key.bytes") as f:
            he.from_bytes_rotate_key(f.read())

    print(f"Public Keys loaded from {key_path}")

    return he


def _get_storage_path() -> str:
    user_id = get_user_id()
    storage_path = os.path.join("server", "storage", str(user_id))
    if not os.path.exists(storage_path):
        os.makedirs(storage_path)

    return storage_path


def _get_document_path() -> str:
    storage_path = _get_storage_path()
    return os.path.join(storage_path, "documents.json")


def _get_key_path() -> str:
    storage_path = _get_storage_path()
    return os.path.join(storage_path, "public_key.zip")
