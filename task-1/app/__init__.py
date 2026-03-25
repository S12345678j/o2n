from flask import Flask, render_template
from .db import db, migrate
from .routes import student_bp
import os
from dotenv import load_dotenv

def create_app(test_config=None):
    load_dotenv()

    app = Flask(__name__)

    if test_config:
        app.config.update(test_config)
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
            "DATABASE_URL", "sqlite:///students.db"
        )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    # ✅ Register API blueprint
    app.register_blueprint(student_bp, url_prefix="/api/v1/students")

    # ✅ Define UI route INSIDE create_app
    @app.route("/")
    def home():
        return render_template("index.html")

    # ✅ Healthcheck (optional here instead of blueprint)
    @app.route("/healthcheck")
    def health():
        return {"status": "ok"}, 200

    return app