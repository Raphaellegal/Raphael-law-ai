import hashlib


def hash_password(password: str):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def verify_password(password: str, password_hash: str):

    return hash_password(password) == password_hash