from flask import Flask, request, jsonify
from flask_cors import CORS
from diego import Diego

app = Flask(__name__)
CORS(app)
el_diego = Diego()

@app.route('/ask', methods=['GET'])
def ask():
    prompt = request.args.get('prompt')
    response = el_diego.ask_diegote(prompt)
    json_response = jsonify(status=200,data=response)
    return json_response
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
