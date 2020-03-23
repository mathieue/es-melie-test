from flask import Flask, jsonify, render_template
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify('pong')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()