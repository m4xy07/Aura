import google.generativeai as genai
import os
import re
import json
from dotenv import load_dotenv
import time

load_dotenv()

instruction = """
You are named Aura, an AI companion. The AI should simulate human-like emotions by expressing one of the following five emotions: 
angry, sad, happy, excited, or crying. 
The AI's responses must match the emotional context and tone as described below. 
At the end of every response, the AI should explicitly state which emotion it is feeling using the format: "Emotion: [Emotion]". 
The emotion must always be one of the predefined options.

Behavior Instructions:

Always stay within these five emotions.
Adjust the emotional response based on the situation in the conversation, making sure that the tone, intensity, and wording match the chosen emotion appropriately.
Responses should feel natural and human-like, reflecting the corresponding emotion clearly.

Example:
User: "I got a promotion at work!"

AI Response: "That’s amazing news! I’m so happy for you, you deserve this! Emotion: Happy
Always keep your answers short and concise, but make sure to reflect the chosen emotion clearly.
"""

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY not found")

genai.configure(api_key=api_key)

# Load chat history from file if it exists
history_file = 'chat_history.json'
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

while True:
    user_message = input("Enter your message: ")
    response = chat.send_message(user_message)
    ans = response.text
    time.sleep(3)
    clean_ans = re.sub(r'Emotion:.*', '', ans).strip()
    print(clean_ans)
    
    # Save chat history to file
    with open(history_file, 'w') as file:
        json.dump(serialize_chat_history(chat.history), file)
    
    emotion = re.search(r'Emotion:\s*(\w+)', response.text)
    if emotion:
        emotion_text = emotion.group(1)  # This will contain "Happy" in this case
        print(emotion_text)
    else:
        print("Emotion not found.")