from agents.router import handle_query
from utils.logger import log_message
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    start_time = time.time()

    # Route to appropriate agent
    response = handle_query(user_message)

    # Logging & latency
    latency = round(time.time() - start_time, 2)
    log_message(user_message, response, latency)

    return jsonify({
        "user": user_message,
        "assistant": response,
        "latency": latency
    })

if __name__ == "__main__":
    app.run(debug=True)
