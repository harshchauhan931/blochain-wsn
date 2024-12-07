from flask import Flask, jsonify, request
from blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(blockchain.get_chain())

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.json.get('data')
    blockchain.add_block(data)
    return jsonify({"message": "Block added"}), 201

if __name__ == "__main__":
    app.run(port=5000)
