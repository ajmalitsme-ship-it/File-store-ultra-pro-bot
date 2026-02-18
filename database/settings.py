from .connection import db

col = db.settings

async def get_settings():
    return await col.find_one({"_id": "main"}) or {}

async def update_settings(data: dict):
    await col.update_one(
        {"_id": "main"},
        {"$set": data},
        upsert=True
    )

async def set_force_channel(channel_username: str):
    await col.update_one(
        {"_id": "main"},
        {"$set": {"force_channel": channel_username}},
        upsert=True
    )

async def enable_force_join(enable: bool):
    await col.update_one(
        {"_id": "main"},
        {"$set": {"force_join_request": enable}},
        upsert=True
    )
