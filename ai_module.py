import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()

with open('data/prompt.txt', 'r') as file:
    instruction = file.read()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("API_KEY not found")

genai.configure(api_key=api_key)

# Load chat history from file if it exists
history_file = 'data/chat_history.json'
if os.path.exists(history_file):
    with open(history_file, 'r') as file:
        chat_history = json.load(file)
else:
    chat_history = []

model = genai.GenerativeModel('gemini-1.5-flash-latest', system_instruction=instruction)

# Deserialize chat history to the required format
def deserialize_chat_history(history):
    deserialized_history = []
    for item in history:
        deserialized_history.append({
            "role": item["role"],
            "parts": [{"text": item["text"]}]
        })
    return deserialized_history

chat = model.start_chat(history=deserialize_chat_history(chat_history))

def serialize_chat_history(history):
    serialized_history = []
    for item in history:
        serialized_history.append({
            "role": item.role,
            "text": item.parts[0].text
        })
    return serialized_history

def get_response(user_message):
    response = chat.send_message(user_message)
    return response.text, chat.history

def save_chat_history(history):
    with open(history_file, 'w') as file:
        json.dump(serialize_chat_history(history), file)