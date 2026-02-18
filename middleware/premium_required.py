from database.premium import is_premium

async def premium_required(user_id: int):
    return await is_premium(user_id)
