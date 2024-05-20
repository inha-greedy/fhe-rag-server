"""
세션 설정에 사용되는 비즈니스 로직을 담은 코드 페이지입니다.
"""

from typing import Dict
from fastapi import Request


_user_map: Dict[str, str] = {"user_id": "qq"}


def get_user_id() -> int:
    """
    get user_id
    """
    return _user_map.get("user_id")


def set_user_id(request: Request):
    """
    set user_id
    """
    origin = request.headers.get("origin")

    _user_map["user_id"] = origin
