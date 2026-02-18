import hashlib
import hmac
from config import BOT_TOKEN


def verify_telegram_webapp(init_data: str) -> bool:
    """
    Verifies Telegram WebApp initData integrity
    """

    try:
        data_check_string = "\n".join(
            sorted([
                chunk for chunk in init_data.split("&")
                if not chunk.startswith("hash=")
            ])
        )

        received_hash = dict(
            x.split("=") for x in init_data.split("&")
        )["hash"]

        secret_key = hashlib.sha256(BOT_TOKEN.encode()).digest()

        calculated_hash = hmac.new(
            secret_key,
            data_check_string.encode(),
            hashlib.sha256
        ).hexdigest()

        return calculated_hash == received_hash

    except Exception:
        return False
