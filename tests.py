import unittest
import json
from app import app  # No need to import apply_edits

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()
        self.app.testing = True

    def test_json_route(self):
        """Test the /json endpoint."""
        response = self.app.get('/json')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertIn("data", data)
        self.assertIn("descriptions", data["data"])
        self.assertEqual(data["data"]["descriptions"]["app_name"], "Telex Grammar Fixer")

    def test_process_message(self):
        """Test the grammar correction endpoint."""
        payload = {
            "message": "I am goin to scholl.",
            "username": "test_user"
        }

        response = self.app.post("/", data=json.dumps(payload), content_type="application/json")
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)
        self.assertIn("message", data)
        self.assertIn("status", data)
        self.assertEqual(data["status"], "success")

if __name__ == "__main__":
    unittest.main()
