import re
import time
import os
from ai_module import get_response, save_chat_history
from video_module import start_video_thread, emotion_videos
from gtts import gTTS
from playsound import playsound
import config  # Import the shared state

# Start the video display thread
start_video_thread()

# Play the startup video
config.current_emotion = "startup"
time.sleep(5)  # Wait for the startup video to play
config.current_emotion = "idle"

while True:
    user_message = input("Enter your message: ")
    response_text, chat_history = get_response(user_message)
    time.sleep(3)
    clean_ans = re.sub(r'Emotion:.*', '', response_text).strip()
    print(clean_ans)

    
    emotion = re.search(r'Emotion:\s*(\w+)', response_text)
    if emotion:
        config.current_emotion = emotion.group(1).lower()  # Update the current emotion
        print(config.current_emotion)
    else:
        print("Emotion not found.")
        
    # Speak the clean answer using gTTS
    tts = gTTS(text=clean_ans, lang='en', slow=False, tld='co.in')
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")
    
        
    # Save chat history to file
    save_chat_history(chat_history)
    
    # Wait for a while before the next interaction
    config.current_emotion = "idle"
    time.sleep(5)