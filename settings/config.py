import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

JWT_KEY = os.getenv('JWT_KEY')

# print(POSTGRES_USER, POSTGRES_PASSWORD, DB_NAME, DB_HOST, DB_PORT, sep='\n')
