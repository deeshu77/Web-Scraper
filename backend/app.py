from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Backend is running!"


@app.route("/fetch-html", methods=["POST"])
def fetch_html():
    url = "https://www.cricbuzz.com/live-cricket-scorecard/115302/rcb-vs-csk-52nd-match-indian-premier-league-2025"  

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        return jsonify({"html": str(soup)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
