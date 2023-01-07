from flask import Flask, render_template, request, redirect, url_for
# from flask_assets import Environment, Bundle
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
