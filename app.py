from flask import Flask, render_template, request
from datetime import datetime, date, time, timedelta
import requests
import json
import re
import os

app = Flask(__name__)

def convertTime(timestamp):
	result = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ") - timedelta(hours=5)
	result = result.strftime("%B %d, %Y (%a) at %I:%M%p")
	return result
app.jinja_env.globals.update(convertTime=convertTime)

@app.route("/", methods=["GET", "POST"])
def gistlist():

    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        username = request.form['github-username']
        username = re.sub(r'\W+(?<!-)', '', username)
        r = requests.get('https://api.github.com/users/' + username + '/gists')
        gistList = json.loads(r.text or r.content)

        if len(gistList) == 0 or len(username) == 0 or type(gistList) is not list:
            error_message = "Sorry, user does not exist or has no gists :("
            return render_template("index.html", error = error_message)

        return render_template("index.html", username=username, list=gistList)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
