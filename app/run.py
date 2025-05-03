import uvicorn

from .config import FASTAPI_PORT, RELOAD_ON_CHANGE


if __name__ == '__main__':
    uvicorn.run('app.main:app', host='127.0.0.1', port=FASTAPI_PORT, reload=RELOAD_ON_CHANGE)