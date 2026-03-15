from flask import Flask, request, send_file
import yt_dlp
import uuid
import os

app = Flask(__name__)

@app.route("/mp3")
def mp3():

    url = request.args.get("url")
    filename = str(uuid.uuid4()) + ".mp3"

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return send_file(filename, as_attachment=True)


@app.route("/mp4")
def mp4():

    url = request.args.get("url")
    filename = str(uuid.uuid4()) + ".mp4"

    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'outtmpl': filename,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return send_file(filename, as_attachment=True)


app.run(host="0.0.0.0", port=8080)