from app import app
from flask import render_template, request
from app.weather import weather, weather_outfit

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
    else:
        city = "Oslo"

    weather_data, weather_right_now = weather(city)
    outfit_suggestion = weather_outfit()
    return render_template("index.html", weather=weather_data, city=city, weather_right_now=weather_right_now, outfit_suggestion=outfit_suggestion)