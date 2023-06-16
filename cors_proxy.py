from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def proxy(path):
    target_url = request.args.get('url')
    headers = request.headers
    method = request.method

    if target_url:
        response = requests.request(
            method=method,
            url=target_url + path,
            headers=headers,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )

        response_headers = {
            key: value
            for (key, value) in response.headers.items()
            if key.lower() != 'content-encoding'
        }

        return response.content, response.status_code, response_headers

    return jsonify({'error': 'Target URL not provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
