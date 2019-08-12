import requests
import os


def getSegmentName(total = 5, segment_no = 0) :
    return str(segment_no).zfill(total)

# Download Video Url
headers = {'Origin' : 'https://practice.geeksforgeeks.org/', 'Referer' : 'https://practice.geeksforgeeks.org/tracks/PC-W1-I/?batchId=140', 'User-Agent' : 'Samsung'}

total_segments = 2
pad = 5
folder_name = "Analysis-of-Algorithms"
os.mkdir(folder_name)
for segment in range(1, total_segments+1):
    segmentName = getSegmentName(pad, segment)
    url = "https://s3.ap-south-1.amazonaws.com/videoin.gfg.org/courses/1710040b3089af8871fec7b5f545d8c6gfg-AnalysisOfAlgorithm-hlsx1080p/00002/1710040b3089af8871fec7b5f545d8c6gfg-AnalysisOfAlgorithm-hlsx1080pseg_"+ segmentName + ".ts"
    req = requests.get(url, headers=headers)
    req.raise_for_status()
    with open(folder_name + "/" + segmentName + ".ts", 'wb') as fd:
        for chunk in req.iter_content(chunk_size=50000):
            fd.write(chunk)