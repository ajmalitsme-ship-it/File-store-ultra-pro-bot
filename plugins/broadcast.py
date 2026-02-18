from pyrogram import Client, filters
from database.users import get_all_users
from database.admins import is_admin
from database.logs import add_log

@Client.on_message(filters.command("broadcast"))
async def broadcast_handler(client, message):

    if not await is_admin(message.from_user.id):
        return

    if len(message.command) < 2:
        await message.reply("Usage: /broadcast Your message here")
        return

    text = message.text.split(None, 1)[1]

    count = 0

    async for user in get_all_users():
        try:
            await client.send_message(user["user_id"], text)
            count += 1
        except:
            continue

    await add_log(
        action="broadcast",
        user_id=message.from_user.id,
        extra={"total_sent": count}
    )

    await message.reply(f"✅ Broadcast sent to {count} users.")
