from flask import Flask, request, jsonify
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "API Running"

@app.route("/api")
def api():
    url = request.args.get("url")
    if not url:
        return jsonify({"error":"No URL"}),400

    try:
        ydl_opts = {"quiet": True, "skip_download": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        return jsonify({
            "title": info.get("title"),
            "thumbnail": info.get("thumbnail")
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run()
