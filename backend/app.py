from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

from config import Config
from model import db

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

jwt = JWTManager(app)
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return "Backend Running Successfully"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)