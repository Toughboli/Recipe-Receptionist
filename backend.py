import cv2
import time
import os
from openai import OpenAI
import io
import base64 
from PIL import Image


client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
messages = []
model_personality = "Helpful and direct."

def url_in(url,dirname,filename):
    os.system(f"you-get {url} -o {dirname} -O {filename}")
    
    possible_extensions = [".mp4", ".webm", ".avi", ".mov"]  # Add more as needed
    file_path = None
    temp = os.path.join(dirname,filename)

    for ext in possible_extensions:
        full_path = temp + ext
        if os.path.exists(full_path):
            file_path = full_path
            break 

    if file_path is not None:
        path = file_path
        print("PATH NAME: ",path)
        process_video(path)
    else:
        print("ERROR: FILE NOT FOUND")
    

def file_in(path):
    process_video(path)


def process_video(video):
    os.system(f"ffmpeg -i {video} -q:a 0 -map a uploads\\audio.mp3 -y")
    print("Transcribing audio...")
    audio_file= open("uploads\\audio.mp3", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file
    )

    print(transcription.text)

    cap = cv2.VideoCapture(video)

    print("Processing video...")
    index = 0
    frames = []

    ret, frame = cap.read()
    while ret:
        if ret and index % 60 == 0: 
            frame = cv2.resize(frame, (224, 224))
            buffer = io.BytesIO()
            Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).save(buffer, format="JPEG")
            buffer.seek(0)
            base64_encoded = base64.b64encode(buffer.read()).decode()
            frames.append(f"data:image/jpeg;base64,{base64_encoded}")

        ret, frame = cap.read()
        index +=1
        

    cap.release() 
    
    messages.append({"role": "developer", "content": "Your personality is: " + model_personality + ""})
    messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this video and answer user questions, transcribed text is: " + transcription.text + "\n, the user will ask questions."},
                *[{
                    "type": "image_url",
                    "image_url": {
                        "url": base64
                    },
                } for base64 in frames],
            ]
        }
    )
    print("video processed")
    

def ask_question(question):
    print(f"Processing question: {question}")
    messages.append({"role": "user", "content": question})
    completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            stream=True
    )

    ans = ""
    for chunk in completion:
        try:
            ans += chunk.choices[0].delta.content
        except TypeError:
            pass


    messages.append({"role": "assistant", "content": ans})
    
    print("ANSWER: ",ans)
    return ans