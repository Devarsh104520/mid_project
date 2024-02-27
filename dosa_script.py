import json

with open(r'C:\Users\kunal\OneDrive\Desktop\mid_project\example_orders.json', 'r') as f:
    data = json.load(f)

dictionary1 = {}
dictionary2 = {}


for i in data:
    dictionary1[i['phone']] = i['name']
    for j in i['items']:
        dictionary2[j['name']] = j['price']
print(dictionary1)
print(dictionary2)
with open('customers.json', 'w') as f:
    json.dump(dictionary1, f, indent=4)

with open('items.json', 'w') as f:
    json.dump(dictionary2, f, indent=4)
