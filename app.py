# Daniel Downes, downesda
# File: app.py
# Last Edited: 06/07/2026
# Description: REST server that handles getting a 
#              timely greeting
# Usage:
#   ./python3 app.py
# Example Request:
#   http://127.0.0.1:6464/greeting
#   The example returns a timely greeting to the client

from flask import Flask
import datetime

app = Flask(__name__)

HOST = "127.0.0.1"
PORT = 6464
DEFAULT_PATH = "/greeting"

### GET REQUESTS ###


# Responds to the client with a timely greeting
@app.get(DEFAULT_PATH)
def get_default_response():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 11:
        return {"greeting": "Good morning!"}, 200
    if hour >= 12 and hour <= 18:
        return {"greeting": "Good afternoon!"}, 200
    else:
        return {"greeting": "Good evening!"}, 200


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
