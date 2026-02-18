import time

RATE_LIMIT = {}
LIMIT_SECONDS = 5  # 1 request per 5 seconds

async def check_rate_limit(user_id: int):
    now = time.time()

    if user_id in RATE_LIMIT:
        if now - RATE_LIMIT[user_id] < LIMIT_SECONDS:
            return False

    RATE_LIMIT[user_id] = now
    return True
