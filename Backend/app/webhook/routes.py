from flask import Blueprint, json
from app.extensions import mongo
from bson import json_util


# Webhook Receiver
webhook = Blueprint("Webhook", __name__, url_prefix="/webhook")


@webhook.route("/get_all_messages", methods=["GET"])
def get_msgs():
    msgs = mongo.db.webhook.find()
    return json.loads(json_util.dumps(msgs))
