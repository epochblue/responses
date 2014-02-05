import json
import yaml

from flask import Flask, request
from flask.helpers import make_response
from flask.templating import render_template


app = Flask(__name__)
app.debug = True

responses = {}

try:
    with open('responses.yaml', 'r') as f:
        responses = yaml.load(f.read())
except Exception:
    pass


@app.route('/')
def index():
    routes = responses.keys() if responses else None
    response = make_response(render_template('index.txt', routes=routes))
    response.headers['Content-Type'] = 'text/plain'
    return response


@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def catch_all(path):
    response_info = responses.get(path)
    method = request.method

    if not response_info:
        status_code = 404
        response = make_response(render_template('error_404.txt', path=path))
        response.headers['Content-Type'] = 'text/plain'

    elif method not in response_info.keys():
        status_code = 405
        response = make_response(render_template('error_405.txt', path=path, method=method))
        response.headers['Content-Type'] = 'text/plain'

    else:
        response_meta = responses[path][method]
        status_code = response_meta['status_code']
        resp = response_meta['response'] if response_meta['response'] else {}
        response = make_response(
            json.dumps(
                resp,
                indent=2,
                separators=(',', ':'),
                sort_keys=True
            ))
        response.headers['Content-Type'] = 'application/json'

    return response, status_code


if __name__ == '__main__':
    app.run()
