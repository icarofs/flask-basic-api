from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [{
    'name': 'My Wonderful Store',
    'items': [{
        'name': 'My Item',
        'price': 15.99
    }]
}]


@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {'name': request_data['name'], 'items': []}
    stores.append(new_store)
    return jsonify(new_store)


@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify(({'message': 'store not found'}))


@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass


app.run(port=5000)
