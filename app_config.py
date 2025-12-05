# config.py 

import os
from dotenv import load_dotenv

load_dotenv()

class get_api:
    API_KEY = os.getenv('API_KEY') # Secret from .env
    TIMEOUT = 30
    DEBUG = os.getenv('DEBUG', 'FALSE').upper() == 'TRUE'

