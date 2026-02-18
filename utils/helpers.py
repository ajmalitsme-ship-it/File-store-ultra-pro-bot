from datetime import datetime
import secrets
import string


# ==========================================
# 🔹 Human Readable File Size
# ==========================================

def format_bytes(size: int) -> str:
    power = 1024
    units = ["B", "KB", "MB", "GB", "TB"]
    n = 0

    while size >= power and n < len(units) - 1:
        size /= power
        n += 1

    return f"{round(size, 2)} {units[n]}"


# ==========================================
# 🔹 Format Datetime
# ==========================================

def format_time(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


# ==========================================
# 🔹 Generate Random Token
# ==========================================

def generate_token(length: int = 32) -> str:
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))


# ==========================================
# 🔹 Standard Success / Error Text
# ==========================================

def success(msg: str) -> str:
    return f"✅ {msg}"


def error(msg: str) -> str:
    return f"❌ {msg}"


# ==========================================
# 🔹 Safe Integer Parser
# ==========================================

def to_int(value, default=0):
    try:
        return int(value)
    except Exception:
        return default
