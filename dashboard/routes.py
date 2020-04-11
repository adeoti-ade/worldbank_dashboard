from dashboard import app

# from flask import Flask
# app = Flask(__name__)

from flask import render_template

@app.route("/")
def index():
    return render_template('index.html')

# @app.route("/")
# def get_news():
#     return "no news is good news"

if __name__ == '__main__':
    app.run(port=5000, debug=True)