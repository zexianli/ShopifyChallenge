## Getting Started:
First you need to create a virtual environment to run the application, then install the dependencies. 

Run these commands inside the directory:
### For Linux:
```
python3 -m venv flaskApp
source flaskApp/bin/activate
pip3 install --upgrade pip
pip install Flask
```

### For Windows:
```
py -3 -m venv flaskApp
flaskApp\Scripts\activate
pip3 install --upgrade pip
```

Once you have installed all the requirements stated above, you can run the Flask application with the following command:
```
python -m main run
```

## Using the CRUD

After opening the link to the CRUD. You can access the directory by going to 
```
http://127.0.0.1:8080/inventory
```
### *This link will show all the current items in inventory*


## Operations

### ADD
```
http://127.0.0.1:8080/inventory/add
```

### Update
```
http://127.0.0.1:8080/inventory/edit
```

### Delete
This url also shows the reason why an item was removed
```
http://127.0.0.1:8080/inventory/delete
```