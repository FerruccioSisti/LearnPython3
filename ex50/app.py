from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')

def hello_world():
    greeting = "World"
    #Set the variables used in the html file as a parameter
    return render_template("index.html", greeting = greeting)

if __name__ == "__main__":
    app.run()
