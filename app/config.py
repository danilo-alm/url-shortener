import os
from dotenv import load_dotenv


load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_DATABASE = os.getenv('MONGO_DATABASE')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION')
API_HOST = os.getenv('API_HOST')
API_PORT = int(os.getenv('API_PORT'))
RELOAD_ON_CHANGE = os.getenv('RELOAD_ON_CHANGE', 'true').lower() == 'true'