# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os
from dotenv import load_dotenv
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#Instantiate dotenv and set constants
load_dotenv()
DB_HOST= os.getenv('DB_HOST')
DB_PORT= os.getenv('DB_PORT')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_SCHEMA= os.getenv('DB_SCHEMA')
DB_USERNAME= os.getenv('DB_USERNAME')
DB_PASSWORD= os.getenv('DB_PASSWORD')

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = f"ibmi://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}?current_schema={DB_SCHEMA}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
DATABASE_CONNECT_OPTIONS = {}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = os.getenv('APP_SESSION')

# Secret key for signing cookies
SECRET_KEY = os.getenv('APP_SECRET')