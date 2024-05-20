"""
세션 설정에 사용되는 비즈니스 로직을 담은 코드 페이지입니다.
"""

from fastapi import Request


USER_MAP = {"sequence": 1000}


def get_user_id() -> int:
    """
    get user_id
    """
    try:
        return USER_MAP["user_id"]

    except KeyError:
        return 999


def set_user_id(request: Request):
    """
    set user_id
    """
    origin = request.headers.get("origin")
    agent = request.headers.get("user-agent")
    user_key = f"origin:{origin}::agent:{agent}"
    print(f"{user_key=}")

    if user_key not in USER_MAP:
        # sequence를 가져와 업데이트합니다
        new_number = USER_MAP["sequence"] + 1
        USER_MAP["sequence"] = new_number

        # 가져온 sequence를 이용해 새 user를 등록합니다
        USER_MAP[user_key] = new_number

    USER_MAP["user_id"] = USER_MAP[user_key]
