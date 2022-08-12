import os
import json

from flask import Flask, request
from redis import StrictRedis
from typing import Text, Optional, Dict, Any

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_DB = os.environ.get("REDIS_DB", 1)

# Init Flask app.
app = Flask(__name__)
# Init Redis client.
redis_client = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

def get_current_user() -> Optional[Dict[Text, Any]]:
    """Retrieve the current user from intermediate storage."""
    encoded_user = redis_client.get("user")
    if encoded_user:
        return json.loads(encoded_user)
    else:
        return None

def store_user(user: Dict[Text, Any]) -> None:
    """Store a users details to our intermediate storage."""
    redis_client.set("user", json.dumps(user))

@app.route('/', methods=["GET"])
def greet():
    """Send a welcoming message to the user."""

    user = get_current_user()
    if user is not None:
        return "Hello, {}!".format(user.get("name"))
    else:
        return "Hello, unknown stranger!"

@app.route('/', methods=["POST"])
def save_name():
    """Change a users details, most importantly his name."""
    user = request.json
    store_user(user)
    return "I'll try to remember your name, {}!".format(user.get("name"))
