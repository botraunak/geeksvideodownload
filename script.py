import requests
import os

# Folder name where you want to download video
folder_name = "Analysis-of-Algorithms"

# Headers to Download Video Url
headers = {'Origin' : 'https://practice.geeksforgeeks.org/', 'Referer' : 'https://practice.geeksforgeeks.org/tracks/PC-W1-I/?batchId=140', 'User-Agent' : 'Samsung'}

try:
    os.mkdir(folder_name)
except:
    print "Couldn't create folder"

def downloadSegment(path, segment, pad):
    host = "https://s3.ap-south-1.amazonaws.com/videoin.gfg.org/courses/" + path
    req = requests.get(url, headers=headers)
    req.raise_for_status()
    with open(folder_name + "/" + str(segment).zfill(pad) + ".ts", 'wb') as fd:
        for chunk in req.iter_content(chunk_size=50000):
            fd.write(chunk)

def downloadPlaylist(url):            
    req = requests.get(url, headers = headers)
    req.raise_for_status()
    with open(folder_name + "/playlist.m3u8", 'wb') as fd:
        for chunk in req.iter_content(chunk_size=50000):
            fd.write(chunk)


url = "https://s3.ap-south-1.amazonaws.com/videoin.gfg.org/courses/1710040b3089af8871fec7b5f545d8c6gfg-AnalysisOfAlgorithm-hlsx1080p.m3u8"
downloadPlaylist(url)

# Read playlist and download video
f = open(folder_name + '/playlist.m3u8')
line = f.readline()
fd = open(folder_name + "/all.txt", "wb")

segment = 1
pad = 5

while line:
    if(line.startswith("1710040b3089af8871fec7b5f545d8c6gfg-AnalysisOfAlgorithm-hlsx1080p/")):
        print "Downloading Segment " + line + "..."
        downloadSegment(line.replace("\n", ""), segment, pad)
        fd.write("file " + str(segment).zfill(pad) + ".ts\n")
        segment += 1
    # use realine() to read next line
    line = f.readline()
f.close()