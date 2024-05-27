from flask import Flask, request, jsonify
from flask_cors import CORS
from api import extract
from api import predict

app = Flask(__name__)
CORS(app)

@app.route('/prever', methods=['POST'])
def domain_info():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'URL parameter is required in JSON payload'}), 400
    
    url = data['url']
    info = extract.get_domain_info(url)
    results=predict.prever(info)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
