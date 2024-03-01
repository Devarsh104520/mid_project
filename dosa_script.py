import json

def process_orders(input_file):
    # Initialize dictionaries for customers and items
    customers = {}
    items = {}

    # Read orders from the input file
    with open(input_file, 'r') as file:
        orders_data = json.load(file)

    # Process each order
    for order in orders_data:
        # Extract and update customer information
        phone = order['phone']
        name = order['name']
        customers[phone] = name
        
        # Extract and update item information
        for item in order['items']:
            item_name = item['name']
            item_price = item['price']
            
            if item_name not in items:
                items[item_name] = {'price': item_price, 'orders': 1}
            else:
                items[item_name]['orders'] += 1

    # Write the processed data to new JSON files
    with open('customers.json', 'w') as file:
        json.dump(customers, file, indent=4)
    
    with open('items.json', 'w') as file:
        json.dump(items, file, indent=4)

# Assuming 'example_orders.json' is the input file
input_file_path = r'C:\Users\kunal\OneDrive\Desktop\mid_project\example_orders.json'
process_orders(input_file_path)

print("Processing complete. 'customers.json' and 'items.json' have been created.")

