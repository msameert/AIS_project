# backend/config.py
import os

class Config:
    # Save DB in project folder
    SQLALCHEMY_DATABASE_URI ="postgresql://postgres.mjyymhtsmpmyjzqbflnw:niyagray8765435@aws-1-ap-southeast-2.pooler.supabase.com:5432/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    