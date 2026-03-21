from flask import Flask, request, send_file
import yt_dlp
import os
import subprocess   # ✅ add this import

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)


@app.route("/")
def home():
    return "Y2G Downloader API Running"


# ✅ ADD IT HERE (new route)
@app.route("/check")
def check():
    try:
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)


@app.route("/mp3")
def mp3():
    url = request.args.get("url")

    if not url:
        return "No URL provided"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'ffmpeg_location': 'ffmpeg',  # ✅ important
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        mp3_file = filename.rsplit(".", 1)[0] + ".mp3"
        return send_file(mp3_file, as_attachment=True)

    except Exception as e:
        return f"ERROR: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
