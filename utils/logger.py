import logging
from datetime import datetime
from pyrogram import Client
from config import LOG_CHANNEL_ID, LOG_TO_FILE


# ==========================================
# 🔹 Python Logging Setup (File Logging)
# ==========================================

if LOG_TO_FILE:
    logging.basicConfig(
        filename="bot.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
else:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )


# ==========================================
# 🔹 Telegram Log Sender
# ==========================================

async def send_log(
    bot: Client,
    title: str,
    message: str,
    level: str = "INFO"
):
    """
    Sends structured log to Telegram log channel
    """

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    formatted_text = (
        f"<b>{title}</b>\n\n"
        f"{message}\n\n"
        f"<b>Time:</b> {timestamp}"
    )

    # Console/File Logging
    if level == "ERROR":
        logging.error(message)
    elif level == "WARNING":
        logging.warning(message)
    else:
        logging.info(message)

    # Telegram Channel Logging
    if not LOG_CHANNEL_ID:
        return

    try:
        await bot.send_message(
            chat_id=LOG_CHANNEL_ID,
            text=formatted_text,
            parse_mode="HTML",
            disable_web_page_preview=True
        )
    except Exception as e:
        logging.error(f"Failed to send log to Telegram: {e}")
