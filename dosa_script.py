import json

def process_orders(input_file):
    customers = {}
    items = {}

    with open(input_file, 'r') as file:
        orders_data = json.load(file)

    for order in orders_data:
        phone = order['phone']
        name = order['name']
        customers[phone] = name
        
        for item in order['items']:
            item_name = item['name']
            item_price = item['price']
            
            if item_name not in items:
                items[item_name] = {'price': item_price, 'orders': 1}
            else:
                items[item_name]['orders'] += 1

    with open('customers.json', 'w') as file:
        json.dump(customers, file, indent=4)
    
    with open('items.json', 'w') as file:
        json.dump(items, file, indent=4)

input_file_path = r'C:\Users\kunal\OneDrive\Desktop\mid_project\example_orders.json'
process_orders(input_file_path)

print("Processing complete. 'customers.json' and 'items.json' have been created.")

