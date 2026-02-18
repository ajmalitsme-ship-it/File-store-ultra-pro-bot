from datetime import datetime
from .connection import db

col = db.logs


# 🔹 Add Log Entry
async def add_log(
    action: str,
    user_id: int = None,
    target_id: int = None,
    extra: dict = None
):
    """
    action: type of action (e.g., 'add_admin', 'broadcast', 'file_upload')
    user_id: who performed the action
    target_id: affected user/file
    extra: optional additional data
    """

    await col.insert_one({
        "action": action,
        "performed_by": user_id,
        "target_id": target_id,
        "extra": extra or {},
        "timestamp": datetime.utcnow()
    })


# 🔹 Get Logs (Latest First)
async def get_logs(limit: int = 50):
    return col.find({}).sort("timestamp", -1).limit(limit)


# 🔹 Get Logs by Action
async def get_logs_by_action(action: str, limit: int = 50):
    return col.find(
        {"action": action}
    ).sort("timestamp", -1).limit(limit)


# 🔹 Get Logs by User
async def get_logs_by_user(user_id: int, limit: int = 50):
    return col.find(
        {"performed_by": user_id}
    ).sort("timestamp", -1).limit(limit)


# 🔹 Count Logs
async def count_logs():
    return await col.count_documents({})


# 🔹 Clear Logs (Dangerous - Admin Only)
async def clear_logs():
    await col.delete_many({})
