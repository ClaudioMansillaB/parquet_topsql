import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# DB configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', 5432),
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

# Folders routes
INPUT_DIR = os.path.join('data', 'input')
OUTPUT_DIR = os.path.join('data', 'output')

# See if the folders exist
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)