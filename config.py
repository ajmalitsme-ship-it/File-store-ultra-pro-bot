import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


# ==========================================================
# 🔹 TELEGRAM BOT CONFIGURATION
# ==========================================================

API_ID = int(os.getenv("API_ID", 27806628))
API_HASH = os.getenv("API_HASH", "25d88301e886b82826a525b7cf52e090")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8425633488:AAFWj_B5YLm-4JdYHZAM1atUUyK-ohuNAI4")

BOT_USERNAME = os.getenv("BOT_USERNAME", "file_store_bot")
OWNER_ID = int(os.getenv("OWNER_ID", 8525952693))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "funnytamilan")


# ==========================================================
# 🔹 DATABASE CONFIGURATION
# ==========================================================

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://Bosshub:JMaff0WvazwNxKky@cluster0.l0xcoc1.mongodb.net/?appName=Cluster0")
DATABASE_NAME = os.getenv("DATABASE_NAME", "file_store_bot")

# Optional Redis (for high traffic scaling)
REDIS_URL = os.getenv("REDIS_URL", None)


# ==========================================================
# 🔹 WEB PANEL CONFIGURATION
# ==========================================================

WEB_URL = os.getenv("WEB_URL", "https://file-store-ultra-pro-bot.onrender.com")

FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY, "8d5c54afbfd5d480274d661f60f6c7a9d8d302184e3232d5")

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "0007")

SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "True") == "True"
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"


# ==========================================================
# 🔹 SECURITY SETTINGS
# ==========================================================

SECRET_KEY = os.getenv("SECRET_KEY", "change_this_super_secret_key")

ENABLE_SIGNED_LINKS = os.getenv("ENABLE_SIGNED_LINKS", "True") == "True"

DEFAULT_LINK_EXPIRY = int(os.getenv("DEFAULT_LINK_EXPIRY", 3600))  # 1 hour

MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 2097152000))  # 2GB


# ==========================================================
# 🔹 LOGGING CONFIGURATION
# ==========================================================

LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", 0))

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

LOG_TO_FILE = os.getenv("LOG_TO_FILE", "True") == "True"

LOG_FOLDER = os.getenv("LOG_FOLDER", "logs")


# ==========================================================
# 🔹 FORCE SUBSCRIBE SETTINGS
# ==========================================================

FORCE_SUBSCRIBE_ENABLED = os.getenv("FORCE_SUBSCRIBE_ENABLED", "True") == "True"

DEFAULT_FORCE_CHANNEL = os.getenv("DEFAULT_FORCE_CHANNEL", "True")

DEFAULT_FORCE_JOIN = os.getenv("DEFAULT_FORCE_JOIN", "True") == "True"


# ==========================================================
# 🔹 PREMIUM SYSTEM SETTINGS
# ==========================================================

PREMIUM_ENABLED = os.getenv("PREMIUM_ENABLED", "True") == "True"

PREMIUM_DEFAULT_DAYS = int(os.getenv("PREMIUM_DEFAULT_DAYS", 30))


# ==========================================================
# 🔹 RATE LIMIT SETTINGS
# ==========================================================

RATE_LIMIT_ENABLED = os.getenv("RATE_LIMIT_ENABLED", "True") == "True"

RATE_LIMIT_PER_MINUTE = int(os.getenv("RATE_LIMIT_PER_MINUTE", 10))


# ==========================================================
# 🔹 SERVER / DEPLOYMENT SETTINGS
# ==========================================================

HOST = os.getenv("HOST", "0.0.0.0")

PORT = int(os.getenv("PORT", 8000))

DEBUG = os.getenv("DEBUG", "False") == "True"

WORKERS = int(os.getenv("WORKERS", 2))  # Gunicorn workers


# ==========================================================
# 🔹 DEPLOYMENT FLAGS
# ==========================================================

USE_NGINX = os.getenv("USE_NGINX", "True") == "True"

USE_CLOUDFLARE = os.getenv("USE_CLOUDFLARE", "False") == "True"

BACKUP_DIR = os.getenv("BACKUP_DIR", "backups")

BACKUP_COMPRESS = os.getenv("BACKUP_COMPRESS", "True") == "True"


# ==========================================================
# 🔹 VALIDATION CHECK (OPTIONAL SAFETY)
# ==========================================================

def validate_config():
    required = {
        "API_ID": API_ID,
        "API_HASH": API_HASH,
        "BOT_TOKEN": BOT_TOKEN,
        "OWNER_ID": OWNER_ID,
        "MONGO_URI": MONGO_URI,
    }

    missing = [key for key, value in required.items() if not value]

    if missing:
        raise ValueError(f"Missing required config values: {', '.join(missing)}")
