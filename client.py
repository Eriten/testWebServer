from flask import Flask, request, make_response, jsonify

def handle_json_request():
    return jsonify({
        'message': 'Good Morning'
    })

def handle_no_accept_request():
    return '<p>Hello World</p>'

APPLICATION = Flask(__name__)
@APPLICATION.route('/', methods=['POST', 'GET'])
def single_endpoint():
    accept_headers = request.headers.get('accept')
    if not accept_headers or '*/*' in accept_headers:
        return handle_no_accept_request()
    if 'application/json' in accept_headers:
        return handle_json_request()
    return jsonify({'message': 'Only accept application/json or no accept header'}), 400
    

if __name__ == '__main__':
    APPLICATION.run(debug=True, host='0.0.0.0')
