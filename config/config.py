# config.py
import os
from dotenv import load_dotenv

#To set the environment variable ENV, you can use the command line:
# export ENV=production
env = os.getenv('ENV', 'development')  # By default, use 'development' if ENV is not set

if env == 'production':
    load_dotenv(dotenv_path='.env.prod')
else:
    load_dotenv(dotenv_path='.env')

# Load environment variables from the .env file
# Example of using an environment variable
BASE_URL = os.getenv('BASE_URL', 'https://default-api-url.com')

