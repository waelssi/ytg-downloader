from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)


@app.route("/")
def home():
    return "Y2G Downloader API Running"


@app.route("/mp3")
def mp3():
    url = request.args.get("url")

    if not url:
        return "No URL provided"

    ydl_opts = {
        "format": "bestaudio",
        "cookiefile": "cookies.txt",
        "outtmpl": DOWNLOAD_FOLDER + "/%(title)s.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320"
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    mp3_file = filename.rsplit(".", 1)[0] + ".mp3"

    return send_file(mp3_file, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
