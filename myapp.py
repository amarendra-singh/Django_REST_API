import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"
headers = {'content-type':'application/json'}

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    
    r = requests.get(URL, data = json_data)
    data = r.json()
    print(data)
# get_data()
#---------------------------------------------------------
def post_data():
    data = {
        'name' : 'dfdsfd',
        'roll' : 100,
        'city' : 'aaaa'
    }
    json_data = json.dumps(data)
    r = requests.post(URL, headers = headers, data = json_data)
    data = r.json()
    print(data)
post_data()
#---------------------------------------------------------
def update_data():
    data = {
        'id':3,
        'name':"Laxman",
        'city':"Kailash"
    }
    json_data = json.dumps(data)
    r = requests.put(URL, data=json_data)
    data = r.json()
    print(data)
# update_data()
#---------------------------------------------------------
# def delete_data():
#     data = {'id': 4}
#     json_data = json.dumps(data)
#     r = requests.delete(URL, data = json_data)
#     data = r.json()
#     print(data)

# delete_data()