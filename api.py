from flask import Flask, jsonify, request
# from analysing import analyse
from main import analyse

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
async def welcome():
    
    requestt = request.get_json()
    response = analyse(requestt['query'], requestt['history'])
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)