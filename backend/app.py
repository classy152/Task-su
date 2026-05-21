from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
import os

from backend.config import Config
from backend.model import db
from backend.routes.auth import auth_bp

app = Flask(__name__)

app.config.from_object(Config)

print("DATABASE URL:", app.config.get("SQLALCHEMY_DATABASE_URI"))

db.init_app(app)

jwt = JWTManager(app)
bcrypt = Bcrypt(app)

@app.route("/")
def home():
    return "Backend Running Successfully"

app.register_blueprint(auth_bp, url_prefix="/auth")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)