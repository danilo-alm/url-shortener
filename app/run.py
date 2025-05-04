import uvicorn

from .config import API_HOST, API_PORT, RELOAD_ON_CHANGE


if __name__ == '__main__':
    uvicorn.run('app.main:app', host=API_HOST, port=API_PORT, reload=RELOAD_ON_CHANGE)