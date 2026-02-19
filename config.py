import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================================
# 🔹 TELEGRAM BOT CONFIGURATION
# ==========================================================

API_ID = int(os.getenv("API_ID", 27806628))
API_HASH = os.getenv("API_HASH", "25d88301e886b82826a525b7cf52e090")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8425633488:AAFWj_B5YLm-4JdYHZAM1atUUyK-ohuNAI4")
OWNER_ID = int(os.getenv("OWNER_ID", 8525952693))


# ==========================================================
# 🔹 DATABASE CONFIGURATION
# ==========================================================

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Bosshub:JMaff0WvazwNxKky@cluster0.l0xcoc1.mongodb.net/?appName=Cluster0")
DATABASE_NAME = os.getenv("DATABASE_NAME", "file_store_bot")


# ==========================================================
# 🔹 DOMAIN & ROUTES
# ==========================================================
WEB_URL = os.getenv(
    "WEB_URL",
    "https://file-store-ultra-pro-bot.onrender.com"
)
DOMAIN = os.getenv(
    "DOMAIN",
    "https://file-store-ultra-pro-bot.onrender.com"
)

ADMIN_PANEL_PATH = os.getenv("ADMIN_PANEL_PATH", "/admin")
STREAM_PATH = os.getenv("STREAM_PATH", "/stream")

ADMIN_PANEL_URL = f"{DOMAIN}{ADMIN_PANEL_PATH}"
STREAM_BASE_URL = f"{DOMAIN}{STREAM_PATH}"


# ==========================================================
# 🔹 START MESSAGE CONFIGURATION
# ==========================================================

# Must be direct public HTTPS image URL
START_IMAGE_URL = os.getenv(
    "START_IMAGE_URL",
    "https://telegra.ph/file/your-image.jpg"
)

START_CAPTION = os.getenv(
    "START_CAPTION",
    "Welcome {first} to Ultra File Store Pro 🚀"
)


# ==========================================================
# 🔹 WEB PANEL CONFIGURATION
# ==========================================================

SECRET_KEY = os.getenv("SECRET_KEY", "H44PBHTWWP4LS0N5")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "H44PBHTWWP4LS0N5")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "H44PBHTWWP4LS0N5")


# ==========================================================
# 🔹 LOGGING CONFIGURATION
# ==========================================================

LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", -1003559364122))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


# ==========================================================
# 🔹 SERVER CONFIGURATION
# ==========================================================

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
DEBUG = os.getenv("DEBUG", "False") == "True"
WORKERS = int(os.getenv("WORKERS", 2))


# ==========================================================
# 🔹 CONFIG VALIDATION
# ==========================================================

def validate_config():
    required = {
        "API_ID": API_ID,
        "API_HASH": API_HASH,
        "BOT_TOKEN": BOT_TOKEN,
        "OWNER_ID": OWNER_ID,
        "MONGO_URI": MONGO_URI,
        "DOMAIN": DOMAIN,
        "SECRET_KEY": SECRET_KEY,
        "FLASK_SECRET_KEY": FLASK_SECRET_KEY,
        "ADMIN_PASSWORD": ADMIN_PASSWORD,
        "LOG_CHANNEL_ID": LOG_CHANNEL_ID,
    }

    missing = [k for k, v in required.items() if not v]

    if missing:
        raise ValueError(
            f"Missing required configuration values: {', '.join(missing)}"
)
