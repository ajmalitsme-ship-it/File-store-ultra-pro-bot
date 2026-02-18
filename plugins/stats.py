from pyrogram import Client, filters
from middleware.rate_limit import check_rate_limit
from database.admins import is_admin, count_admins
from database.users import count_users
from database.files import count_files
from database.premium import count_premium_users
from database.logs import count_logs


@Client.on_message(filters.command("stats"))
async def stats_handler(client, message):

    user_id = message.from_user.id

    # Rate limit protection
    if not await check_rate_limit(user_id):
        return

    # Admin protection
    if not await is_admin(user_id):
        await message.reply("🚫 You are not authorized to use this command.")
        return

    # Fetch statistics
    total_users = await count_users()
    total_files = await count_files()
    total_admins = await count_admins()
    total_premium = await count_premium_users()
    total_logs = await count_logs()

    stats_text = (
        "📊 **Bot Statistics Dashboard**\n\n"
        f"👥 Total Users: `{total_users}`\n"
        f"📂 Stored Files: `{total_files}`\n"
        f"👑 Admins: `{total_admins}`\n"
        f"💎 Premium Users: `{total_premium}`\n"
        f"📝 System Logs: `{total_logs}`\n\n"
        "⚡ System running normally."
    )

    await message.reply(stats_text)
