import requests
import os
import subprocess
import time

# Folder name where you want to download video
folder_name = input("Enter the folder name: ")
url = input("Enter the video m3u8 file: ")

# Headers to Download Video Url
headers = {
    'Origin': 'https://www.geeksforgeeks.org', 
    'Referer': 'https://www.geeksforgeeks.org', 
    'User-Agent': 'Samsung'
}

# Create folder safely
os.makedirs(folder_name, exist_ok=True)

def downloadSegment(path, segment, pad):
    host = "https://cdnvideos.geeksforgeeks.org/hls/" + path
    req = requests.get(host, headers=headers)
    req.raise_for_status()
    with open(os.path.join(folder_name, f"{str(segment).zfill(pad)}.ts"), 'wb') as fd:
        for chunk in req.iter_content(chunk_size=50000):
            fd.write(chunk)

def downloadPlaylist(url):            
    req = requests.get(url, headers=headers)
    req.raise_for_status()
    with open(os.path.join(folder_name, "playlist.m3u8"), 'wb') as fd:
        for chunk in req.iter_content(chunk_size=50000):
            fd.write(chunk)

# Download the playlist            
downloadPlaylist(url)

# Read playlist and download video
with open(os.path.join(folder_name, 'playlist.m3u8'), 'r') as f:
    lines = f.readlines()

with open(os.path.join(folder_name, "all.txt"), "w") as fd:
    segment = 1
    pad = 5
    for line in lines:
        line = line.strip()
        if not line.startswith("#"):
            print(f"Downloading Segment {line}...")
            downloadSegment(line, segment, pad)
            fd.write(f"file {str(segment).zfill(pad)}.ts\n")
            segment += 1

# Merge Video
time.sleep(5.0)
os.chdir(folder_name)
subprocess.call(['ffmpeg', '-f', 'concat', '-i', 'all.txt', '-c', 'copy', 'all.ts'])
subprocess.call(['ffmpeg', '-i', 'all.ts', '-acodec', 'copy', '-vcodec', 'copy', 'all.mp4'])