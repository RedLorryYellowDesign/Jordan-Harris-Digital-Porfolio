from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about-me')
def about_me():
    return render_template('about-me.html')

@app.route('/projects')
def projects():
    return render_template('projects')

if __name__ == '__main__':
    app.run(debug=True)
