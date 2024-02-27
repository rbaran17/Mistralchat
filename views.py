from flask import Blueprint, request, jsonify
import requests

# Create a Blueprint for your views
bp = Blueprint('main', __name__)

@bp.route('/chat', methods=['POST'])
def chat():
    # Replace 'YOUR_MISTRAL_API_KEY' with your actual Mistral API key
    MISTRAL_API_KEY = 'NP9R2gUJiRZGnaOSOIta5veOhYS0tOjz'

    # Define the endpoint URL
    url = 'https://api.mistral.ai/v1/chat/completions'

    # Define the request headers including the bearer token
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {MISTRAL_API_KEY}'
    }

    # Get the user message from the request
    user_message = request.json.get('message')

    # Define the request body with the model and user message
    payload = {
        "model": "mistral-large-latest",
        "messages": [{"role": "user", "content": user_message}]
    }

    # Send the POST request to the Mistral API
    response = requests.post(url, json=payload, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Successful request
        return jsonify(response.json()), 200
    else:
        # Handle errors
        return jsonify({"error": response.text}), response.status_code
