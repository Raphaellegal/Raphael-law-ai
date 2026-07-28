from dataclasses import dataclass
from typing import Optional


@dataclass
class User:

    id: Optional[int]

    full_name: str

    email: str

    password_hash: str

    category: str

    role: str

    verified: bool = False

    verification_status: str = "not_required"

    subscription: str = "free"