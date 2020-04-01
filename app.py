from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from elasticsearch import Elasticsearch

DEBUG = True

es = Elasticsearch(
    ['localhost'],
    port=9292,
)

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping():
    results = es.cluster.health()
    return jsonify(results)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    q = request.args.get('q')

    body = {
        "query": {
            "query_string": {
                "query": q
            }
        }
    }

    results = es.search(body=body)
    return jsonify(results)


if __name__ == '__main__':
    app.run()