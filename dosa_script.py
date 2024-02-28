import json

with open(r'C:\Users\kunal\OneDrive\Desktop\mid_project\example_orders.json', 'r') as f:
    data = json.load(f)

dictionary1 = dict(map(lambda i: (i['phone'], i['name']), data))
dictionary2 = dict(map(lambda i: (i['name'], i['price']), [item for sublist in [i['items'] for i in data] for item in sublist]))


print(dictionary2)

with open('customers.json', 'w') as f:
    json.dump(dictionary1, f, indent=4)

with open('items.json', 'w') as f:
    json.dump(dictionary2, f, indent=4)
