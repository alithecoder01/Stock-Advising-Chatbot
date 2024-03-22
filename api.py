from flask import Flask, jsonify, request
from analysing import analyse

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
async def welcome():
    re = await analyse("hi")
    return jsonify({'response': re})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

# app = Flask(__name__)

# @app.route('/<int:number>/')
# def incrementer(number):
#     return "Incremented number is " + str(number+1)

# @app.route('/<string:name>/')
# def hello(name):
#     return "Hello " + name

# app.run()