# Geeks for Geeks Video Downloader

# ffmpeg command to merge all .ts files
```
ffmpeg -f concat -i all.txt -c copy all.ts
```

# ffmpeg commang to convert all.ts to .mp4
```
ffmpeg -i all.ts -acodec copy -vcodec copy all.mp4
```