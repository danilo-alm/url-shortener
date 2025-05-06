from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, FileResponse

import app.base62 as base62
from .hash_url import hash_url
from .db import get_collection
from .cache import r
from .models import URLRequest, EncodedURLResponse, URLEntry
from .config import REDIS_EXPIRATION_SECONDS


collection = get_collection()
app = FastAPI()


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
        url_entry = URLEntry(_id=encoded_id, original_url=original_url)
        collection.insert_one(url_entry.model_dump(mode='json', by_alias=True))

    r.setex(encoded_id, REDIS_EXPIRATION_SECONDS, original_url)
    return EncodedURLResponse(encodedUrl=encoded_id)


@app.get('/{encoded}')
def redirect_url(encoded: str):
    original_url = r.getex(encoded, ex=REDIS_EXPIRATION_SECONDS)
    
    if not original_url:
        doc = collection.find_one({'_id': encoded}, {'original_url': 1})
        if not doc:
            raise HTTPException(status_code=404, detail='Invalid URL')
        original_url = doc['original_url']
        r.setex(encoded, REDIS_EXPIRATION_SECONDS, original_url)

    return RedirectResponse(url=original_url, status_code=308)