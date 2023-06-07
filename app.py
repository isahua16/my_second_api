from dbhelpers import run_statement
from flask import Flask, request
import json

app = Flask(__name__)

@app.post('/api/item')
def create_item():
    name = request.json.get('item_name')
    description = request.json.get('item_description')
    price = request.json.get('item_price')
    results = run_statement('CALL create_item(?,?,?)', [name, description, price])
    if(type(results) == list):
        json_results = json.dumps(results, default=str)
        return json_results
    else:
        'Something is wrong. Try again'

@app.get('/api/item')
def get_items():
    results = run_statement('CALL get_items()')
    if(type(results) == list):
        json_results = json.dumps(results, default=str)
        return json_results
    else:
        'Something is wrong. Try again'

@app.patch('/api/item')
def update_price():
    id = request.json.get('item_id')
    price = request.json.get('item_price')
    results = run_statement('CALL update_price(?,?)', [id, price])
    if(type(results) == list):
        json_results = json.dumps(results, default=str)
        return json_results
    else:
        'Something is wrong. Try again'

@app.delete('/api/item')
def delete_item():
    id = request.json.get('item_id')
    run_statement('CALL delete_item(?)', [id])
    return 'Item Successfully Deleted'

app.run(debug=True)
