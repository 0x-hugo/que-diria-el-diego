from flask import Flask, request, jsonify
from flask_cors import CORS
from diego import Diego

app = Flask(__name__)
el_diegote = Diego()
CORS(app)

@app.route('/ask', methods=['GET'])
def ask():
    prompt = request.args.get('prompt')
    response = el_diegote.ask_diegote(prompt)
    json_response = jsonify(status=200,data=response)
    print("diego respuesta", json_response)
    return json_response
    
if __name__ == '__main__':
    app.run(port=5005, debug=True)
