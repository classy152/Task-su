from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

from config import Config
from model import db
from route.auth import auth_bp

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

jwt = JWTManager(app)
bcrypt = Bcrypt(app)

app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/')
def home():
    return "Backend Running Successfully"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)