import google.generativeai as genai
import os
import re
import json
from dotenv import load_dotenv
import time
import cv2
import subprocess
import threading

load_dotenv()

with open('data/prompt.txt', 'r') as file:
    instruction = file.read()

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

# Dictionary to map emotions to video files
emotion_videos = {
    "angry": "resources/angry.mp4",
    "sad": "resources/sad.mp4",
    "happy": "resources/idle.mp4",
    "excited": "resources/excited.mp4",
    "crying": "resources/crying.mp4",
    "idle": "resources/idle.mp4",
    "startup": "resources/idle.mp4"
}

# Variable to store the current emotion
current_emotion = "idle"

# Function to play a video in full-screen loop
def play_video_in_fullscreen(video_path):
    cap = cv2.VideoCapture(video_path)
    cv2.namedWindow("AI Face Display", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("AI Face Display", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    while True:
        ret, frame = cap.read()
        if not ret:  # Restart video if it reaches the end
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        cv2.imshow("AI Face Display", frame)
        
        # Exit condition for the window; can use 'q' to quit if needed
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Function to display the appropriate video based on emotion
def display_emotion_face(emotion):
    video_path = emotion_videos.get(emotion, emotion_videos["idle"])
    play_video_in_fullscreen(video_path)

# Function to play the startup video
def play_startup_video():
    play_video_in_fullscreen(emotion_videos["startup"])

# Start a separate thread to handle video display
def video_display_thread():
    global current_emotion
    while True:
        display_emotion_face(current_emotion)
        time.sleep(0.1)

# Play the startup video
play_startup_video()

# Start the video display thread
video_thread = threading.Thread(target=video_display_thread)
video_thread.daemon = Truevideo_thread.start() # type: ignore
video_thread.start()

while True:
    user_message = input("Enter your message: ")
    response = chat.send_message(user_message)
    ans = response.text
    time.sleep(15)
    clean_ans = re.sub(r'Emotion:.*', '', ans).strip()
    print(clean_ans)
    
    # Use espeak to speak the AI response
    subprocess.run(['espeak', '-s', '140', '-p', '50', clean_ans], shell=True)
    
    # Save chat history to file
    with open(history_file, 'w') as file:
        json.dump(serialize_chat_history(chat.history), file)
    
    emotion = re.search(r'Emotion:\s*(\w+)', response.text)
    if emotion:
        current_emotion = emotion.group(1).lower()  # Update the current emotion
        print(current_emotion)
        time.sleep(10)  # Wait for 10 seconds before reverting to idle
        current_emotion = "idle"
    else:
        print("Emotion not found.")
    