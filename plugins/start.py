from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import WEB_URL, START_PHOTO
from database.users import add_user
from middleware.force_sub import check_force
from middleware.rate_limit import check_rate_limit

@Client.on_message(filters.command("start"))
async def start(client, message):

    if not await check_rate_limit(message.from_user.id):
        return

    await add_user(message.from_user.id)

    if not await check_force(client, message.from_user.id):
        await message.reply("Please join required channel first.")
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "⚙️ Open Control Panel",
            web_app=WebAppInfo(url=WEB_URL)
        )]
    ])

    await message.reply_photo(
        photo=START_PHOTO,
        caption="🚀 Welcome to Advanced File Store Bot",
        reply_markup=keyboard
    )
