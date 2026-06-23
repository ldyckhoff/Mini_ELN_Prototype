from __future__ import annotations

import hashlib
from datetime import datetime
from uuid import uuid4


def make_id(prefix: str, *seed_parts: object) -> str:
    """Create a compact readable ID from time, optional context, and random salt."""
    seed = "|".join(str(part) for part in seed_parts if part is not None)
    seed = f"{datetime.now().isoformat(timespec='microseconds')}|{seed}|{uuid4().hex}"
    digest = hashlib.sha1(seed.encode("utf-8")).hexdigest()[:10]
    return f"{prefix}_{digest}"


def slugify(value: str) -> str:
    cleaned = []
    last_was_separator = False
    for char in value.lower().strip():
        if char.isalnum():
            cleaned.append(char)
            last_was_separator = False
        elif not last_was_separator:
            cleaned.append("_")
            last_was_separator = True
    slug = "".join(cleaned).strip("_")
    return slug or "item"

