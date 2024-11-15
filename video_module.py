import cv2
import threading
import config  # Import the shared state

# Dictionary to map emotions to video files
emotion_videos = {
    "angry": "resources/angry.mp4",
    "sad": "resources/sad.mp4",
    "happy": "resources/happy.mp4",
    "idle": "resources/idle.mp4",
    "startup": "resources/startup.mp4"
}

# Function to play a video in full-screen loop
def play_video_in_fullscreen():
    current_video_path = emotion_videos[config.current_emotion]
    cap = cv2.VideoCapture(current_video_path)
    cv2.namedWindow("AI Face Display", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("AI Face Display", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    while True:
        ret, frame = cap.read()
        if not ret:  # Restart video if it reaches the end
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = cap.read()
        
        cv2.imshow("AI Face Display", frame)
        
        # Check for emotion change
        if current_video_path != emotion_videos[config.current_emotion]:
            current_video_path = emotion_videos[config.current_emotion]
            cap.release()
            cap = cv2.VideoCapture(current_video_path)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Function to start the video display thread
def start_video_thread():
    video_thread = threading.Thread(target=play_video_in_fullscreen)
    video_thread.daemon = True
    video_thread.start()