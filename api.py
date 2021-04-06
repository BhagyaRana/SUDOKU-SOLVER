from flask import Flask, request, jsonify
from functions import solve
from flask_cors import CORS, cross_origin
from time import time

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = False

@app.route('/api/backtracking', methods=['POST'])
@cross_origin()
def backtracking():
    board = request.get_json()
    start = time()
    solve(board, 0, 0)
    end = time()
    return jsonify({"board": board, "time": (end - start)})

app.run()
