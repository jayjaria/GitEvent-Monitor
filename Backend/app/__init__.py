from flask import Flask
from app.extensions import mongo
from flask_cors import CORS
from app.webhook.routes import webhook
from app.webhook_action.routes import action_webhook
import os


def run_app():

    app = Flask(__name__)

    # registering all the blueprints
    app.register_blueprint(webhook)
    app.register_blueprint(action_webhook)
    app.config["MONGO_URI"] = os.environ.get(
        "MONGO_URI", "mongo://localhost:27017/database"
    )
    mongo.init_app(app)
    CORS(app)

    @app.route("/")
    def hello():
        return "Hi"

    return app
