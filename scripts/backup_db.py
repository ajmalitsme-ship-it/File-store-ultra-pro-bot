import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "file_store_bot")
BACKUP_DIR = os.getenv("BACKUP_DIR", "backups")
COMPRESS = os.getenv("BACKUP_COMPRESS", "True") == "True"


def create_backup():

    try:
        # Create backup directory
        os.makedirs(BACKUP_DIR, exist_ok=True)

        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(BACKUP_DIR, f"{DATABASE_NAME}_{timestamp}")

        print("🔄 Starting MongoDB backup...")

        command = [
            "mongodump",
            "--uri", MONGO_URI,
            "--db", DATABASE_NAME,
            "--out", backup_path
        ]

        subprocess.run(command, check=True)

        if COMPRESS:
            print("📦 Compressing backup...")
            subprocess.run(
                ["tar", "-czf", f"{backup_path}.tar.gz", "-C", BACKUP_DIR, f"{DATABASE_NAME}_{timestamp}"],
                check=True
            )
            subprocess.run(["rm", "-rf", backup_path], check=True)

        print(f"✅ Backup created successfully at: {backup_path}.tar.gz" if COMPRESS else backup_path)

    except subprocess.CalledProcessError as e:
        print(f"❌ Backup failed: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    create_backup()
