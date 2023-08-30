from dotenv import load_dotenv
from os import getenv

load_dotenv()
load_dotenv(dotenv_path="./.env.public")

API_KEY = getenv('API_KEY')

FIREBASE_apiKey = getenv('FIREBASE_apiKey')
FIREBASE_authDomain = getenv('FIREBASE_authDomain')
FIREBASE_projectId = getenv('FIREBASE_projectId')
FIREBASE_storageBucket = getenv('FIREBASE_storageBucket')
FIREBASE_appId = getenv('FIREBASE_appId')

FIREBASE_ROOT_COLLECTION_NAME = getenv('FIREBASE_ROOT_COLLECTION_NAME')
