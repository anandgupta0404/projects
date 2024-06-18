from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
data = [
    {'id': 1, 'name': 'Item 1', 'description': 'This is item 1'},
    {'id': 2, 'name': 'Item 2', 'description': 'This is item 2'},
]

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data), 200

# Get a single item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    return jsonify(item), 200

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item), 201

# Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    updated_data = request.get_json()
    item.update(updated_data)
    return jsonify(item), 200

# Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)