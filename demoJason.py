# demoJason.py

import json
with open('myinfo.json', encoding='UTF8') as f:
     data = json.load(f)
 
print(type(data))
print(data)


d = {"name":"Tom", "birth":"0525", "age": 30}
json_data = json.dumps(d)
print(json_data)