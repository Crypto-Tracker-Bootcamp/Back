from flask import Blueprint

# Define a blueprint for the main routes
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return 'Welcome to the Crypto Tracker!'

@main.route('/crypto/<string:symbol>')
def get_crypto(symbol):
    return f'Showing data for: {symbol}'
