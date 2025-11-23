# backend/config.py
import os

class Config:
    # Save DB in project folder
    SQLALCHEMY_DATABASE_URI ="postgresql://postgres:niyagray8765435@aws-0-db.mjyymhtsmpmyjzqbflnw.supabase.co:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "my-secret-key-123"  # For login later