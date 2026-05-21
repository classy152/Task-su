from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
import os

from backend.config import Config
from backend.model import db

# IMPORT ONLY AUTH FIRST
# from backend.routes.auth import auth_bp

app = Flask(__name__)

# LOAD CONFIG
app.config.from_object(Config)

# DEBUG CHECK
print("DATABASE URL:", app.config.get("SQLALCHEMY_DATABASE_URI"))

# INITIALIZE EXTENSIONS
db.init_app(app)

jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# ROOT ROUTE
@app.route("/")
def home():
    return "Backend Running Successfully"

# REGISTER ONLY AUTH FIRST
# app.register_blueprint(auth_bp, url_prefix="/auth")

# RUN APP
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)