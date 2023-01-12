# Imports
from flask import Flask, render_template, request, redirect, url_for # Imports base flask dependantsies
# from flask_assets import Environment, Bundle
from flask_caching import Cache # Allows for a Cache
from flask_compress import Compress # Allows for asset Compresion

# Flast Configuration
config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)
compress = Compress()

# Compression of assets to improve performance
def start_app():
    app = Flask(__name__)
    compress.init_app(app)
    return app

# API Call to root directory
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
