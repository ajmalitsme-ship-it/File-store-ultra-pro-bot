from database.admins import is_admin

async def admin_required(user_id: int):
    return await is_admin(user_id)
