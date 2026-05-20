from app import app
from flask import render_template
import requests

@app.route("/")
def index():
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=59.91&longitude=10.75&current_weather=true")
    data = response.json()
    return render_template("index.html", weather=data)

