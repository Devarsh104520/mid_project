## Restaurant Order Analysis Tool

This script is designed to analyze order data from a restaurant's JSON file and output customer details and item statistics in separate JSON files.

## Overview

The provided Python script takes a JSON-formatted order file as input and extracts key information about customers and their orders. The output is twofold:

- A `customers.json` file that maps customer phone numbers to their names.
- An `items.json` file that includes each item's price and the total number of times it has been ordered.

## Requirments

You will need to have Python installed on your machine to execute the script. The script relies exclusively on Python's built-in libraries, so no additional installations are necessary.

## Design and Implementation: 

The code is designed to process a JSON file containing a list of orders, where each order includes a customer's phone number, name, and a list of items purchased. It extracts and organizes this information into two separate JSON files, customers.json and items.json, for further use or analysis. Here's a breakdown of its design and logic:

1.Function Design 

-Function Definition: The process_orders function is designed to take a single parameter, input_file, which is the path to the JSON file containing the order data.

-Dictionaries for Data Storage:
  1.customers: A dictionary to store customer information, using phone numbers as keys and customer names as values. This structure makes it easy to access a customer's name by their phone number and ensures that each 
  customer is uniquely identified by their phone number.
  2.items: A dictionary to store information about items ordered. The keys are item names, and the values are dictionaries containing the price of the item and the number of times it has been ordered. This structure 
  allows for easy updates to the order count and access to item pricing.

2.Data Processing

-Reading JSON Input: The script opens and reads the input JSON file using Python's built-in json.load() function, which converts the JSON file into a Python data structure (in this case, a list of dictionaries, with each dictionary representing an order).

-Iterating Through Orders: For each order in the input data, the script performs two main tasks:
   1.Customer Data Extraction: Extracts the customer's phone number and name, then stores this information in the customers dictionary. This part ensures that the customer information is recorded uniquely based on phone 
   numbers.
   2.Item Data Aggregation: For each item in an order, the script checks if the item is already in the items dictionary:
     -If not, it adds the item with its price and initializes the order count to 1.
     -If the item already exists, it increments the order count for that item by 1.

3.Writing Output JSON Files

-Output to customers.json: The script writes the customers dictionary to a file named 'customers.json', formatting it with an indentation of 4 spaces for readability. This file maps customer phone numbers to names.

-Output to items.json: Similarly, the items dictionary is written to a file named 'items.json'. This file includes a record of each item, its price, and how many times it was ordered.

4.Execution and Output

-File Paths: The script defines input_file_path with the path to the input JSON file. This path is hardcoded in the script and points to a specific location on a Windows system. Users of the script would need to modify 
 this path to match the location of their input file.

-Function Call and Completion Message: After defining the input_file_path, the script calls process_orders(input_file_path) to process the specified input file. Upon successful execution, it prints a message indicating 
 that processing is complete and that the output files have been created.

5.Design Considerations

-Flexibility: The script is designed to process any JSON file that follows the expected format, making it flexible for various datasets.
-Efficiency: By using dictionaries for data storage, the script ensures efficient access and update operations, crucial for processing potentially large datasets.
-Simplicity: The code structure is straightforward, making it easy to understand and modify for different requirements or data formats.
## Instructions

To use the script:

1. Ensure the JSON order file is located in the same directory as the script or provide the full path to the file.
2. Verify that the order file is formatted correctly, similar to the `example_orders.json` structure.
3. Update the script with the correct path to your JSON file:
   ```python
   input_file_path = 'your_orders_file_path.json'
4. Run the script using the following command:
   python dosa_script.py
   After successful execution, check the output directory for customers.json and items.json files.
## Input File Format
Your input JSON file should follow this format:

     
     [
     {
       "phone": "1234567890",
       "name": "John Doe",
       "items": [
         {
           "name": "Item 1",
           "price": 9.99
         },
         {
           "name": "Item 2",
           "price": 15.99
         }
       ]
     },
     // Additional orders...
     ]

## Output Files

-customers.json: Contains a mapping of customer phone numbers to their names.

-items.json: Contains details of each item, including its price and the number of orders.
## Notes

-The script overwrites customers.json and items.json files if they exist in the output directory.

-Ensure the input JSON file is correctly formatted to avoid processing errors.
   
     
