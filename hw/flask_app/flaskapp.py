from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("home.html",
                           home_heading = "Welcome!")

@app.route('/about')
def about():
    return render_template("about.html",
                           about_heading = "Hey there, it's Varvara!",
                           about_subtitle = "I'm here to tell you about my passion for languages, as well as some aspects of my academic and \
                                professional background.")