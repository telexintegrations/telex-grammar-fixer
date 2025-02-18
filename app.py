from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your webhook endpoint
@app.route('/telex-webhook', methods=['POST'])
def process_message():
    data = request.json  # Get JSON data from Telex
    original_message = data.get("message", "")
    username = data.get("username", "Unknown")

    # Simulating grammar correction (You can replace this with an API call)
    corrected_message = original_message.replace("hopes", "hope").replace("is work", "works")

    # Prepare response to send back to Telex
    response_data = {
        "event_name": "grammar_correction",
        "message": corrected_message,
        "status": "success",
        "username": username
    }

    return jsonify(response_data)  # Send corrected message back to Telex

if __name__ == '__main__':
    app.run(port=5000)  # Run Flask app on port 5000
