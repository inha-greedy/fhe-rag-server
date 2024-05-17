import os
import zipfile
from Pyfhel import Pyfhel

from .enc import set_he_context


def save_key(contents: bytes) -> None:

    # 디렉토리 없으면 단듦
    storage_path = "./server/storage/key"

    if not os.path.exists(storage_path):
        os.makedirs(storage_path)

    # insert public key
    key_path = "./server/storage/key/public_keys.zip"

    with open(key_path, "wb") as fp:
        fp.write(contents)


def load_public_key() -> None:

    he = Pyfhel()

    zip_file_path = "./server/storage/key/public_keys.zip"

    with zipfile.ZipFile(zip_file_path, "r") as zipf:
        with zipf.open("context.bytes") as f:
            he.from_bytes_context(f.read())
        with zipf.open("public_key.bytes") as f:
            he.from_bytes_public_key(f.read())
        with zipf.open("relin_key.bytes") as f:
            he.from_bytes_relin_key(f.read())
        with zipf.open("rotate_key.bytes") as f:
            he.from_bytes_rotate_key(f.read())

    set_he_context(he=he)
    print(f"Public Keys loaded from {zip_file_path}")
