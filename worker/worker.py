import time, os, subprocess
from redis import Redis

redis_conn = Redis(host="queue", port=6379)

VIDEOS_FOLDER = "/data"

while True:
    filepath = redis_conn.lpop("video_queue")
    if filepath:
        filepath = filepath.decode()
        print(f"Processing video: {filepath}")

        # Convert MP4 -> WEBM
        base = os.path.splitext(filepath)[0]
        webm_file = base + ".webm"
        try:
            subprocess.run(["ffmpeg", "-i", filepath, webm_file], check=True)
            print(f"Converted to: {webm_file}")
        except Exception as e:
            print(f"Error converting video: {e}")

        # Generate thumbnail
        thumb_file = base + ".jpg"
        try:
            subprocess.run(["ffmpeg", "-i", filepath, "-ss", "00:00:01.000", "-vframes", "1", thumb_file], check=True)
            print(f"Thumbnail created: {thumb_file}")
        except Exception as e:
            print(f"Error generating thumbnail: {e}")

        print(f"Processing complete for {filepath}")
    else:
        time.sleep(1)

