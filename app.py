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

@app.post('/api/employee')
def create_employee():
    name = request.json.get('employee_name')
    position = request.json.get('employee_position')
    wage = request.json.get('employee_wage')
    results = run_statement('CALL create_employee(?,?,?)', [name, position, wage])
    if(type(results) == list):
        json_results = json.dumps(results, default=str)
        return json_results
    else:
        'Something is wrong. Try again'

@app.get('/api/employee')
def get_employee():
    id = request.args.get('employee_id')
    results = run_statement('CALL get_employee(?)', [id])
    if(type(results) == list):
        json_results = json.dumps(results, default=str)
        return json_results
    else:
        'Something is wrong. Try again'

@app.patch('/api/employee')
def update_wage():
    id = request.json.get('employee_id')
    wage = request.json.get('employee_wage')
    results = run_statement('CALL update_wage(?,?)', [id, wage])
    if(type(results) == list):
        json_results = json.dumps(results, default=str)
        return json_results
    else:
        'Something is wrong. Try again'

@app.delete('/api/employee')
def delete_employee():
    id = request.json.get('employee_id')
    run_statement('CALL delete_employee(?)', [id])
    return 'Employee Successfully Deleted'

app.run(debug=True)
