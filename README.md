# Telex Grammar Fixer

Telex Grammar Fixer is a modifier integration for the Telex platform that automatically corrects grammatical errors in messages before they are sent.

## Features
- Automatically fixes grammatical errors in messages.
- Works with Telex webhooks.
- Supports multiple languages.
- Provides real-time corrections before messages are sent.

## Deployment
This integration is hosted on **Railway** using a **Dockerfile**.

## Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Set up a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python app.py
   ```

## Deployment on Railway
1. Install the Railway CLI:
   ```sh
   curl -fsSL https://railway.app/install.sh | sh
   ```
2. Login to Railway:
   ```sh
   railway login
   ```
3. Create a new project and deploy:
   ```sh
   railway init
   railway up
   ```

## API Endpoints
- `POST /` : Receives messages, corrects grammar, and returns the corrected message.
- `GET /json` : Returns integration metadata.

## Environment Variables
Ensure the following environment variables are set:
- `SAPLING_API_KEY` - API key for the grammar correction service.

## Testing
To test locally, use a tool like Postman or cURL:
```sh
curl -X POST http://localhost:5000/ -H "Content-Type: application/json" -d '{"message": "This are a bad sentence"}'
```
Expected response:
```json
{
    "event_name": "grammar_correction",
    "message": "This is a bad sentence",
    "status": "success",
    "username": "Unknown"
}
```

## Screenshots
Below are screenshots demonstrating how the integration works in a Telex channel:

### Before Sending
The message before being processed by the integration:
![Before Sending](ScreenShot-1.png)

### After Sending
The message after being corrected by the integration:
![After Sending](ScreenShot-2.png)

## Contributing
Pull requests are welcome. Please follow best coding practices and ensure proper documentation.

## License
This project is licensed under the MIT License.

