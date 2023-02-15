from flask import Flask, render_template, request, redirect, url_for,jsonify
# from flask_debugtoolbar import DebugToolbarExtension
# from flask_assets import Environment, Bundle
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__)

# # the toolbar is only enabled in debug mode:
# app.debug = True

# # set a 'SECRET_KEY' to enable the Flask session cookies
# app.config['SECRET_KEY'] = '<replace with a secret key>'

# toolbar = DebugToolbarExtension(app)

app.config.from_mapping(config)
cache = Cache(app)

@app.route('/')
def index():
    return render_template('index.html')

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=False)
