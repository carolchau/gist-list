# [Gist List](http://gist-list.herokuapp.com/)
A website that displays a list of all public gists from a given GitHub user. It uses Python2.7 and Flask.

## Motivation
It can get tedious to keep track of students' work that were exported as gists. The intention of this website is to make it easier to input a student's GitHub username and see all gists associated with the student.

Although this application can only list a single user's gists at a time, I plan on building on this, and adding log-in/register functionality, the ability to create a class roster, and displaying students' gists.  

## Setup
Clone this repository:
```Shell
git clone https://github.com/carolchau/gist-list.git
```

Optional, but highly recommended: Create an isolated Python environment to setup this project. I used `virtualenv`

Move to the project's root directory and install all dependencies:
```Shell
pip install -r requirements.txt
```

## Usage
Once the dependencies are installed, you can start the application by running:
```Shell
python app.py
```

Access the application at `localhost:5000`
