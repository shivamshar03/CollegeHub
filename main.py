from flask import Flask, render_template
import json
import os

my_dir = os.path.dirname(__file__)
json_file_path = os.path.join(my_dir, 'busboard.json')
with open(json_file_path, 'r') as f:
        bus_number = json.load(f)["bus_no"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/busboard")
def busboard():
    return render_template('busboard.html', bus_number=bus_number)


@app.route("/acadmic_calender")
def calender():
    return render_template('calender.html')


@app.route("/events")
def events():
    return render_template('events.html')


@app.route("/news")
def news():
    return render_template('news.html')


@app.route("/lost-found")
def lost_found():
    return render_template('lostfound.html')


@app.route("/community-chat")
def community_chat():
    return render_template('underdev.html')


@app.route("/feedback")
def feedback():
    return render_template('underdev.html')


app.run()
