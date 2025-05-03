import os
from dotenv import load_dotenv


load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_DATABASE = os.getenv('MONGO_DATABASE')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION')
FASTAPI_PORT = int(os.getenv('FASTAPI_PORT', 8000))
RELOAD_ON_CHANGE = os.getenv('RELOAD_ON_CHANGE', 'true').lower() == 'true'