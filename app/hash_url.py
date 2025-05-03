import hashlib


def hash_url(url: str) -> int:
    """Hashes a URL to a unique integer."""
    md5_hash = hashlib.md5(url.encode()).digest()
    return int.from_bytes(md5_hash[:6], 'big')