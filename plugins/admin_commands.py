from pyrogram import Client, filters
from config import OWNER_ID
from database.admins import add_admin, remove_admin
from database.logs import add_log


@Client.on_message(filters.command("addadmin"))
async def add_admin_cmd(client, message):

    if message.from_user.id != OWNER_ID:
        return

    if len(message.command) < 2:
        await message.reply("Usage: /addadmin user_id")
        return

    new_admin = int(message.command[1])
    await add_admin(new_admin)

    await add_log(
        action="add_admin",
        user_id=message.from_user.id,
        target_id=new_admin
    )

    await message.reply("✅ Admin added.")


@Client.on_message(filters.command("removeadmin"))
async def remove_admin_cmd(client, message):

    if message.from_user.id != OWNER_ID:
        return

    if len(message.command) < 2:
        await message.reply("Usage: /removeadmin user_id")
        return

    admin_id = int(message.command[1])
    await remove_admin(admin_id)

    await add_log(
        action="remove_admin",
        user_id=message.from_user.id,
        target_id=admin_id
    )

    await message.reply("✅ Admin removed.")
