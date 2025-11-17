# backend/config.py
import os

class Config:
    # Save DB in project folder
    SQLALCHEMY_DATABASE_URI = "sqlite:///ais.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "my-secret-key-123"  # For login later