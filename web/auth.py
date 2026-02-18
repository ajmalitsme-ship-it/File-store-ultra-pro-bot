from flask import session, redirect
from functools import wraps
from config import OWNER_ID


def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if not session.get("admin"):
            return redirect("/login")
        return await func(*args, **kwargs)
    return wrapper
