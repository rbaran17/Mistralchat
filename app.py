from flask import Flask, request, jsonify, render_template
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os

app = Flask(__name__)

api_key = os.environ.get("NP9R2gUJiRZGnaOSOIta5veOhYS0tOjz")
client = MistralClient(api_key=api_key)
model = "mistral-large-latest"

@app.route('/test')
def test():
    return "Test page"  # Assuming you have a chat.html file in your templates folder

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    messages = [ChatMessage(role="user", content=user_message)]
    
    # With streaming
    stream_response = client.chat_stream(model=model, messages=messages)
    response_content = ""
    for chunk in stream_response:
        response_content += chunk.choices[0].delta.content

    return jsonify({"response": response_content})

if __name__ == "__main__":
    app.run(debug=True)
