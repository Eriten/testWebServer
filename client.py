from flask import Flask, request, make_response, jsonify
import json

def handle_json_request():
    return jsonify({
        'message': 'Good Morning'
    })

def handle_no_accept_request(name, helloString):
    return "<p>" + helloString + " " + name + "</p>"

def read_value_by_locale(lang, value):
    # 1. We should handle the case where lang.json doesn't exist
    # 2. Could we override lang.json
    with open('lang.json') as data_file:
        # Handling of invalid json
        lang_file_data = json.load(data_file)
        return lang_file_data[lang][value]

APPLICATION = Flask(__name__)
@APPLICATION.route('/', methods=['POST', 'GET'])
def single_endpoint():
    accept_headers = request.headers.get('accept')
    parameters = request.args
    # Language is universal to all endpoints, preloading
    lang = parameters.get('lang', 'en')
    if not accept_headers or '*/*' in accept_headers:
        name = parameters.get('name', 'World')
        return handle_no_accept_request(name, read_value_by_locale(lang, 'Hello'))
    if 'application/json' in accept_headers:
        return handle_json_request()
    return jsonify({'message': 'Only accept application/json or no accept header'}), 400
    

if __name__ == '__main__':
    APPLICATION.run(debug=True, host='0.0.0.0')
