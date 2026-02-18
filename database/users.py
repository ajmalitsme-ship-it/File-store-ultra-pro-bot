from .connection import db
from datetime import datetime

col = db.users

async def add_user(user_id: int):
    await col.update_one(
        {"user_id": user_id},
        {
            "$setOnInsert": {
                "user_id": user_id,
                "joined_at": datetime.utcnow()
            }
        },
        upsert=True
    )

async def get_user(user_id: int):
    return await col.find_one({"user_id": user_id})

async def get_all_users():
    return col.find({})

async def count_users():
    return await col.count_documents({})
