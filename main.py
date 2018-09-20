from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    title = "User Signup Page"
    return render_template("index.html", title=title)

app.run()    