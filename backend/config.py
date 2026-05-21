import os

db_url = os.getenv("DATABASE_URL")

if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

if "sslmode" not in db_url:
    db_url += "?sslmode=require"

app.config["SQLALCHEMY_DATABASE_URI"] = db_url