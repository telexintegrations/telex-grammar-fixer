from flask import Flask, request, jsonify
import requests
from sapling import SaplingClient
from bs4 import BeautifulSoup
import os
app = Flask(__name__)
from flask_cors import CORS
CORS(app)


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
      "app_logo": "https://th.bing.com/th/id/R.3b52a25bff6073178e8db8df5cf351a6?rik=jyae6pEiWPdsNw&pid=ImgRaw&r=0",
      "app_name": "Telex Grammar Fixer",
      "app_url": "https://telex-grammar-fixer-production.up.railway.app/",
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
        "required": False ,
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
    "target_url": "https://telex-grammar-fixer-production.up.railway.app/"
  }
}

)

SAPLING_API_KEY = os.environ.get("SAPLING_API_KEY")
client = SaplingClient(api_key=SAPLING_API_KEY)


def apply_edits(text, edits):
    """Applies Sapling edits to the original text."""
    text = str(text)
    edits = sorted(edits, key=lambda e: (e['sentence_start'] + e['start']), reverse=True)
    
    for edit in edits:
        start = edit['sentence_start'] + edit['start']
        end = edit['sentence_start'] + edit['end']
        
        if start > len(text) or end > len(text):
            print(f'Edit start:{start}/end:{end} outside of bounds of text:{text}')
            continue
        
        text = text[:start] + edit['replacement'] + text[end:]
    
    return text

@app.route('/', methods=['POST','GET'])
def process_message():
    data = request.json  # Get JSON data from Telex
    original_message = data.get("message", )
    soup = BeautifulSoup(original_message, "html.parser")
    original_message = soup.get_text(separator=" ", strip=True)
   
    username = data.get("username", "Unknown")

    # Send message to Sapling AI for spell check
    try:
        response = client.edits(original_message, session_id="test_session")

        if "edits" in response:
            corrected_message = apply_edits(original_message, response["edits"])
        else:
            corrected_message = original_message  # If API fails, return original

    except Exception as e:
        corrected_message = original_message  # In case of errors, return original
        print("Error:", e)

    # Prepare response to send back to Telex
    response_data = {
        "event_name": "grammar_correction",
        "message": corrected_message,
        "status": "success",
        "username": username
    }

    return jsonify(response_data)
if __name__ == '__main__':
    app.run(debug=True)  # Run Flask app on port 5000
