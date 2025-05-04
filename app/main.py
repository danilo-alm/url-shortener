from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import RedirectResponse, FileResponse

import app.base62 as base62
from .hash_url import hash_url
from .db import get_collection
from .models import URLRequest, URLResponse, URLEntry


collection = get_collection()
app = FastAPI()


@app.get('/')
def serve_index():
    return FileResponse('static/index.html')


@app.post('/shorten')
def shorten_url(url_request: URLRequest, req: Request):
    long_url = str(url_request.url)
    hashed_url = hash_url(long_url)
    encoded_url = base62.encode(hashed_url)

    exists = collection.find_one({'_id': encoded_url})
    if exists:
        short_url = build_shortened_url(encoded_url, req)
        return URLResponse(url=short_url)
    
    url_entry = URLEntry(
        _id=encoded_url,
        original_url=long_url
    )

    doc = url_entry.model_dump(mode='json', by_alias=True)
    collection.insert_one(doc)

    short_url = build_shortened_url(encoded_url, req)
    return URLResponse(url=short_url)


@app.get('/{encoded}')
def redirect_url(encoded: str):
    url_entry = collection.find_one({'_id': encoded}, {'original_url': 1})
    if url_entry:
        original_url = url_entry['original_url']
        return RedirectResponse(url=original_url, status_code=308)
    else:
        return HTTPException(status_code=404, detail=f'Invalid URL')


def build_shortened_url(encoded_url: str, req: Request):
    base_url = str(req.base_url)
    return f'{base_url}{encoded_url}'

