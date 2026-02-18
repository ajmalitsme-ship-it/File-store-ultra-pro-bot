import hashlib
import time
from config import SECRET_KEY


def generate_secure_link(file_id: str, expiry_seconds: int = 3600):

    expire_at = int(time.time()) + expiry_seconds

    raw_string = f"{file_id}:{expire_at}:{SECRET_KEY}"

    signature = hashlib.sha256(raw_string.encode()).hexdigest()

    return f"{file_id}?exp={expire_at}&sig={signature}"


def verify_secure_link(file_id: str, exp: int, sig: str):

    if int(time.time()) > int(exp):
        return False

    raw_string = f"{file_id}:{exp}:{SECRET_KEY}"
    expected_sig = hashlib.sha256(raw_string.encode()).hexdigest()

    return expected_sig == sig
