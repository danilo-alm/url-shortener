from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from pydantic import HttpUrl
from circuitbreaker import circuit
from redis import RedisError

import app.base62 as base62
from .hash_url import hash_url
from .db import get_collection
from .cache import r
from .models import URLRequest, EncodedURLResponse, URLEntry
from .config import REDIS_EXPIRATION_SECONDS


collection = get_collection()
app = FastAPI()


@circuit(failure_threshold=3, recovery_timeout=10, expected_exception=RedisError)
def safe_redis_setex(key, ttl, value):
    r.setex(key, ttl, value)


@circuit(failure_threshold=3, recovery_timeout=10, expected_exception=RedisError)
def safe_redis_getex(key, ttl):
    return r.getex(key, ex=ttl)


@app.get('/')
def serve_index():
    return FileResponse('static/index.html')


@app.post('/shorten')
def shorten_url(url_request: URLRequest):
    original_url = str(url_request.url)
    url_hash = hash_url(original_url)
    encoded_id = base62.encode(url_hash)

    is_new = not collection.find_one({'_id': encoded_id})
    if is_new:
        url_entry = URLEntry(_id=encoded_id, original_url=HttpUrl(original_url))
        collection.insert_one(url_entry.model_dump(mode='json', by_alias=True))

    try:
        safe_redis_setex(encoded_id, REDIS_EXPIRATION_SECONDS, original_url)
    except RedisError:
        pass

    return EncodedURLResponse(encodedUrl=encoded_id)


@app.get('/{encoded}')
def redirect_url(encoded: str):
    original_url = None

    try:
        original_url = safe_redis_getex(encoded, REDIS_EXPIRATION_SECONDS)
    except RedisError:
        pass

    if not original_url:
        doc = collection.find_one({'_id': encoded}, {'original_url': 1})
        if not doc:
            raise HTTPException(status_code=404, detail='Invalid URL')
        original_url = doc['original_url']
        try:
            safe_redis_setex(encoded, REDIS_EXPIRATION_SECONDS, original_url)
        except RedisError:
            pass

    return RedirectResponse(url=original_url, status_code=308)