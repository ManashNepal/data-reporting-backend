import re
from uuid import uuid4

def generate_slug(title: str) -> str:
    base = re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")
    return f"{base}-{uuid4().hex[:8]}"
