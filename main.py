from flask import Flask, render_template, request

db = {}

db["First"] = ["10", "15"]
db["Second"] = ["20", "25"]

removedDB = {}
removedDB["Third"] = "No users"

app = Flask('app')

@app.route('/')
def hello_world():
  return render_template("index.html")
  
@app.route('/inventory')
def inventory_get():
  if request.method != 'GET':
    return '<h1> Invalid method for this url</h1>'
    
  rows = [[key, val[0], val[1]] for key, val in db.items()]
  return render_template("inventory/get.html", rows=rows)

@app.route('/inventory/add', methods=['GET', 'POST'])
def inventory_add():
  if request.method == 'GET':
    rows = [[key, val[0], val[1]] for key, val in db.items()]
    return render_template("inventory/add.html", rows=rows)
  elif request.method == 'POST':
    name = request.form['name']
    price = request.form['price']
    amount = request.form['amount']

    if not name or not price or not amount:
      return '<h1> Make sure the values on the form are valid</h1>'

    if not price.isdigit() or not amount.isdigit():
      return '<h1> Make sure the price or amount are numbers</h1>'

    if name in db:
      return '<h1> Item already exists</h1>'

    if name in removedDB:
      del removedDB[name]
    
    db[name] = [price, amount]
    message = "Successfully added item"
    rows = [[key, val[0], val[1]] for key, val in db.items()]
    return render_template("inventory/add.html", rows=rows, message=message)

@app.route('/inventory/delete', methods=['GET', 'POST'])
def inventory_del():
  if request.method == 'GET':
    rows = [[key, val[0], val[1]] for key, val in db.items()]
    removed = [[key, val] for key, val in removedDB.items()]
    return render_template("inventory/del.html", rows=rows, removed=removed)
  elif request.method == 'POST':
    name = request.form['name']
    reason = request.form['reason']
    
    if not name:
      return '<h1> Make sure the values on the form are valid</h1>'

    if name not in db:
      return '<h1> Item doesn\'t exist</h1>'
    
    del db[name]
    removedDB[name] = reason
    message = f"Removed item {name}"
    rows = [[key, val[0], val[1]] for key, val in db.items()]
    removed = [[key, val] for key, val in removedDB.items()]
    return render_template("inventory/del.html", rows=rows, removed=removed, message=message)

@app.route('/inventory/edit', methods=['GET', 'POST'])
def inventory_update():
  if request.method == 'GET':
    rows = [[key, db[key][0], db[key][1]] for key in db.keys()]
    return render_template("inventory/add.html", rows=rows)
  elif request.method == 'POST':
    name = request.form['name']
    price = request.form['price']
    amount = request.form['amount']

    if not name or not price or not amount:
      return '<h1> Make sure the values on the form are valid</h1>'

    if not price.isdigit() or not amount.isdigit():
      return '<h1> Make sure the price or amount are numbers</h1>'

    if name not in db:
      return '<h1> Item doesn\'t exist</h1>'
    
    db[name] = [price, amount]
  
    message = f"Updated item {name}"
    return render_template("inventory/add.html", message=message)

app.run(host='0.0.0.0', port=8080)