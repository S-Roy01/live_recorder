from pytube import YouTube
import os

f = open("e.txt", "w")
!gdown --id 1EJsJNGOqmpMqJcDsxKJ9duPl1MaUw2jN --output e.txt
while True:
    youtube = YouTube("https://www.youtube.com/channel/UCxHoBXkY88Tb8z1Ssj6CWsQ") 
    # Record lowest resolution stream 
    recording = youtube.streams.first().record(output_path='video1.mp4')
    
    # Check size every 10 seconds 
    while recording.is_recording():
        time.sleep(10)
        file_size = os.path.getsize('video.mp4')
        if file_size > 2000000: # 500MB in byte        
            # Upload current chunk
            !gdown --id 1EJsJNGOqmpMqJcDsxKJ9duPl1MaUw2jN --output video1.mp4            
            
    # Recording finished, upload final chunk        
    !gdown --id 1EJsJNGOqmpMqJcDsxKJ9duPl1MaUw2jN --output video1.mp4
