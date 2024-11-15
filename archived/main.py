import re
import time
import os
import speech_recognition as sr
from ai_module import get_response, save_chat_history
from video_module import start_video_thread, emotion_videos
from gtts import gTTS
from playsound import playsound
import config  # Import the shared state

# Initialize the recognizer
recognizer = sr.Recognizer()

def listen_for_keyword():
    with sr.Microphone() as source:
        print("Listening for keyword 'Hey Aura'...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            if "hey aura" in text:
                print("Keyword detected. Listening for command...")
                return True
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return False

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"Command received: {command}")
            return command
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return ""

# Start the video display thread
start_video_thread()

# Play the startup video
config.current_emotion = "startup"
time.sleep(5)  # Wait for the startup video to play
config.current_emotion = "idle"

while True:
    if listen_for_keyword():
        user_message = listen_for_command()
        if user_message:
            response_text, chat_history = get_response(user_message)
            time.sleep(3)
            clean_ans = re.sub(r'Emotion:.*', '', response_text).strip()
            print(clean_ans)
            
            # Save chat history to file
            save_chat_history(chat_history)
            
            emotion = re.search(r'Emotion:\s*(\w+)', response_text)
            if emotion:
                config.current_emotion = emotion.group(1).lower()  # Update the current emotion
                print(config.current_emotion)
            else:
                print("Emotion not found.")
                
            # Speak the clean answer using gTTS
            tts = gTTS(text=clean_ans, lang='en', slow=False)
            tts.save("response.mp3")
            playsound("response.mp3")
            os.remove("response.mp3")
            
            # Wait for a while before the next interaction
            config.current_emotion = "idle"
            time.sleep(5)