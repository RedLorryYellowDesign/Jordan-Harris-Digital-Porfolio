from flask import Flask, render_template, request, redirect, url_for
from Content import *


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', data1=Profile, data2=Skills)

@app.route('/Design Porfolio')
def LandingPage():
    return render_template('Portfolio.html')

@app.route('/test')
def test():
    #return "Hello World";

    return render_template('hello_world.html', data = data)


if __name__ == '__main__':
    app.run(debug=True)
