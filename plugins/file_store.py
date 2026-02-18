from pyrogram import Client, filters
from config import WEB_URL
from database.files import save_file
from database.logs import add_log
from middleware.rate_limit import check_rate_limit

@Client.on_message(filters.document | filters.video | filters.audio)
async def store_file(client, message):

    if not await check_rate_limit(message.from_user.id):
        return

    file = message.document or message.video or message.audio

    await save_file(
        file.file_id,
        file.file_name,
        message.from_user.id
    )

    await add_log(
        action="file_upload",
        user_id=message.from_user.id,
        extra={"file_name": file.file_name}
    )

    link = f"{WEB_URL}/file/{file.file_id}"

    await message.reply(
        f"✅ File Stored Successfully!\n\n🔗 {link}"
    )
