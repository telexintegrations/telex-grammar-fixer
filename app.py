from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your webhook endpoint

@app.route('/json')
def get_data():
    return jsonify({
  "data": {
    "date": {
      "created_at": "2025-02-18",
      "updated_at": "2025-02-18"
    },
    "descriptions": {
      "app_description": "A grammar fixer that corrects and enhances messages before they are sent.",
      "app_logo": "https://your-app-logo-url.com/logo.png",
      "app_name": "Telex Grammar Fixer",
      "app_url": "https://hng-internship-stage-3-production.up.railway.app/",
      "background_color": "#34A853"
    },
    "integration_category": "Communication & Collaboration",
    "integration_type": "modifier",
    "is_active": True,
    "output": [
      {
        "label": "corrected_text",
        "value": True
      }
    ],
    "key_features": [
      "Automatically fixes grammatical errors in messages.",
      "Works with Telex webhooks.",
      "Supports multiple languages.",
      "Provides real-time corrections before messages are sent."
    ],
    "permissions": {
      "monitoring_user": {
        "always_online": True,
        "display_name": "Grammar Bot"
      }
    },
    "settings": [
      {
        "label": "Correction Level",
        "type": "dropdown",
        "required": True,
        "default": "Medium",
        "options": ["Basic", "Medium", "Advanced"]
      },
      {
        "label": "Language",
        "type": "dropdown",
        "required": True,
        "default": "English",
        "options": ["English", "French", "Spanish"]
      },
      {
        "label": "Enable Auto-Correction",
        "type": "checkbox",
        "required": False,
        "default": "Yes"
      },
      {
        "label": "Notify on Errors",
        "type": "multi-checkbox",
        "required": True,
        "default": "Super-Admin",
        "options": ["Super-Admin", "Admin", "Manager", "Developer"]
      }
    ],
    "target_url": "https://hng-internship-stage-3-production.up.railway.app/api/fix-grammar"
  }
}
)

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
    app.run(debug=True)  # Run Flask app on port 5000
