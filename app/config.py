import os
from dotenv import load_dotenv


load_dotenv()

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
MONGO_USERNAME = os.getenv('MONGO_USERNAME', 'admin')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD', 'secret')
MONGO_DATABASE = os.getenv('MONGO_DATABASE', 'url_shortener')
MONGO_COLLECTION = os.getenv('MONGO_COLLECTION', 'urls')
API_HOST = os.getenv('API_HOST', '127.0.0.1')
API_PORT = int(os.getenv('API_PORT', 8000))
RELOAD_ON_CHANGE = os.getenv('RELOAD_ON_CHANGE', 'true').lower() == 'true'