import os

class Config:
    AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
    DEBUG = True
