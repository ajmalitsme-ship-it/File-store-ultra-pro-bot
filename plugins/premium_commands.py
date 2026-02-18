from pyrogram import Client, filters
from database.admins import is_admin
from database.premium import add_premium
from database.logs import add_log


@Client.on_message(filters.command("addpremium"))
async def add_premium_cmd(client, message):

    if not await is_admin(message.from_user.id):
        return

    if len(message.command) < 3:
        await message.reply("Usage: /addpremium user_id days")
        return

    user_id = int(message.command[1])
    days = int(message.command[2])

    await add_premium(user_id, days)

    await add_log(
        action="add_premium",
        user_id=message.from_user.id,
        target_id=user_id,
        extra={"days": days}
    )

    await message.reply("✅ Premium added.")
