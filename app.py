from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from elasticsearch import Elasticsearch
import os
import sys
import yaml

DEBUG = True

es = Elasticsearch(
    ['localhost'],
    port=9292,
)

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


config_path = os.environ.get('CONFIG_PATH', 'conf')
sys.path.append(config_path)

from searches import *

with open('%s/config.yml' % config_path) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)        

@app.route('/ping', methods=['GET'])
def ping():
    results = es.cluster.health()
    return jsonify(results)

@app.route('/')
def home():
    return render_template('index.html', searches=data['searches'])

@app.route('/search', methods=['GET'])
def search():
    q = request.args.get('q')
    searchid = request.args.get('searchid')

    search = data['searches'][int(searchid)]
    print(search)

    body= getattr(sys.modules[__name__], "dosearch_%s" % search['search'])(q)

    results = es.search(index=search['index'], body=body)
    return render_template('search-results.html', results=results, showField=search['show-field'])

if __name__ == '__main__':
    app.run()