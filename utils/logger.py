import json
from datetime import datetime

def log_message(user_message, response, latency):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_message": user_message,
        "response": response,
        "latency": latency
    }
    with open("chat_logs.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")
