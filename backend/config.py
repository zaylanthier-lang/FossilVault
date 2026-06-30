from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fossilvault.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "fossilvault-secret-key-2026"

    CORS(
        app,
        supports_credentials=True,
        origins=["http://localhost:5173"]
    )

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    return app