from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd29e808cb25a8d4cc3f71ece460c433d'

from dashboard import routes
