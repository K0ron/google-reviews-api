from flask import Flask, jsonify
import requests, os
from flask_cors import CORS
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

cors_origins = os.getenv("CORS_ALLOWED_ORIGINS","")
origin_list = [origin.strip() for origin in cors_origins.split(",") if origin.strip()]

CORS(app, origins=origin_list)


API_KEY = os.getenv("GOOGLE_API_KEY")
PLACE_ID = os.getenv("GOOGLE_PLACE_ID")


@app.route("/api/reviews")
def get_reviews():
    url = f"https://maps.googleapis.com/maps/api/place/details/json?placeid={PLACE_ID}&fields=reviews&key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return jsonify(data.get("result", {}).get("reviews", []))


@app.route("/")
def health():
    return "Google Reviews API is runnung."


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8888))
    app.run(host="0.0.0.0", port=port)
