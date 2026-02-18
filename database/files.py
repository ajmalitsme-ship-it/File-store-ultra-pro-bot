from .connection import db
from datetime import datetime

col = db.files

async def save_file(file_id: str, file_name: str, uploader: int):
    await col.insert_one({
        "file_id": file_id,
        "file_name": file_name,
        "uploaded_by": uploader,
        "uploaded_at": datetime.utcnow()
    })

async def get_file(file_id: str):
    return await col.find_one({"file_id": file_id})

async def delete_file(file_id: str):
    await col.delete_one({"file_id": file_id})

async def count_files():
    return await col.count_documents({})
