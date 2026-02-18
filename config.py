import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

MONGO_URI = os.getenv("MONGO_URI")

WEB_URL = os.getenv("WEB_URL")
START_PHOTO = os.getenv("START_PHOTO")

OWNER_ID = int(os.getenv("OWNER_ID"))
PORT = int(os.getenv("PORT", 8000))
