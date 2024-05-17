from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from .routes.chat import chat_router
from .routes.document import document_router
from .routes.key import key_router
from .services.session import set_user_id
from .services.enc import set_he_context


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(document_router)
app.include_router(key_router)
# set default HE Key
set_he_context()


@app.middleware("http")
async def add_user_id_to_request(request: Request, call_next):
    """
    모든 요청에 대해 사용자 ID를 추가합니다.
    """
    set_user_id(request)
    response = await call_next(request)
    return response
