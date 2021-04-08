from flask import Flask, request, jsonify
from functions import solve1, solve2
from flask_cors import CORS, cross_origin
from time import time

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

@app.route('/api/backtracking', methods=['POST'])
@cross_origin()
def backtracking():
    board = request.get_json()
    start = time()
    solve1(board, 0, 0)
    end = time()
    end -= start
    end *= 10**3
    end = "{:.2f}".format(end)
    return jsonify({"board": board, "time": end})

@app.route('/api/set', methods=['POST'])
@cross_origin()
def set():
    board = request.get_json()
    start = time()
    solve2(board)
    end = time()
    end -= start
    end *= 1000
    end = "{:.2f}".format(end)
    return jsonify({"board": board, "time": end})

app.run()
