import os

class Config:

    db_url = os.environ.get("DATABASE_URL")

    if db_url:

        if db_url.startswith("postgres://"):
            db_url = db_url.replace("postgres://", "postgresql://", 1)

        if "sslmode" not in db_url:
            db_url += "?sslmode=require"

    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")