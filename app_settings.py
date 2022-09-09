import os

from dotenv import load_dotenv

load_dotenv()
AWS_ACCESS_KEY_ID = os.getenv('POSTGRES_HOST')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME')
QUEUE_URL = os.getenv('QUEUE_URL')
