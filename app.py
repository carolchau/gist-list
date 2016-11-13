from flask import Flask, render_template, request
import requests
import json
import re
import dateutil.parser
import datetime

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def gistlist():

    if request.method == "GET":
        return render_template("index.html")
    #button = request.form['submit-username']
    if request.method == "POST":
        username = request.form['github-username']
        username = re.sub(r'\W+(?<!-)', '', username)
        r = requests.get('https://api.github.com/users/' + username + '/gists')
        repoItem = json.loads(r.text or r.content)
        if not repoItem:
            error_message = "Sorry, user does not exist or has no gists :("
            return render_template("index.html", error = error_message)
        return render_template("index.html", username=username, list=repoItem)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)
