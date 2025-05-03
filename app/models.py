from pydantic import BaseModel, HttpUrl, Field

class URLRequest(BaseModel):
    url: HttpUrl

class URLResponse(BaseModel):
    url: HttpUrl

class URLEntry(BaseModel):
    id: str = Field(..., alias='_id')
    original_url: HttpUrl