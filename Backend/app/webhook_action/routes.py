from flask import Blueprint, request, json
from app.extensions import mongo

action_webhook = Blueprint("Webhook_Action", __name__, url_prefix="/action")


@action_webhook.route("/webhook", methods=["POST"])
def git_event():
    if "X-Github-Event" in request.headers:
        event = request.headers["X-Github-Event"]

        # {author} pushed to {to_branch} on {timestamp}

        msg = {}
        if event == "push":

            pusher = request.json.get("pusher")
            head_commit = request.json.get("head_commit")
            ref = request.json.get("ref")
            msg["req_id"] = request.json.get("after")

            if pusher:
                msg["author"] = pusher["name"]
            if head_commit:
                msg["timestamp"] = head_commit["timestamp"]
            if ref:
                msg["to_branch"] = ref.split("/")[-1]

            msg["action"] = "PUSH"

        elif event == "pull_request":

            action = request.json.get("action")
            pull_request = request.json.get("pull_request")
            head = pull_request.get("head")
            base = pull_request.get("base")

            if action == "synchronize":
                return {}, 200

            if pull_request:
                msg["timestamp"] = pull_request["created_at"]
            if head:
                msg["from_branch"] = head["ref"]
            if base:
                msg["to_branch"] = base["ref"]
                msg["author"] = base["label"].split(":")[0]

            msg["action"] = "MERGE" if action == "closed" else "PULL"

        mongo.db.webhook.insert_one(msg)

    return {}, 200
