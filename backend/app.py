from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

from backend.routes.project import projects_bp
from backend.routes.dashboard import dashboard_bp
from backend.routes.auth import auth_bp
from backend.routes.task import tasks_bp

from backend.config import Config
from backend.model import db

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# CREATE TABLES
with app.app_context():
    db.create_all()

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(projects_bp, url_prefix='/projects')
app.register_blueprint(tasks_bp, url_prefix='/tasks')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

@app.route('/')
def home():
    return "Backend Running Successfully"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)