## Restaurant Order Analysis Tool

This script is designed to analyze order data from a restaurant's JSON file and output customer details and item statistics in separate JSON files.

## Overview

The provided Python script takes a JSON-formatted order file as input and extracts key information about customers and their orders. The output is twofold:

- A `customers.json` file that maps customer phone numbers to their names.
- An `items.json` file that includes each item's price and the total number of times it has been ordered.

## Requirments

You will need to have Python installed on your machine to execute the script. The script relies exclusively on Python's built-in libraries, so no additional installations are necessary.

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
## Input file format
    
    [
  {
    "phone": "9292454973",
    "name": "Jeevan",
    "items": [
       {
          "name":"Item 1"
          "price":9.99
       },
       {
          "name":"Item 2"
          "price":10.99
       }
     ]
  },
....
]
## Output Files

-customers.json: Contains a mapping of customer phone numbers to their names.
-items.json: Contains details of each item, including its price and the number of orders.
## Notes

-The script overwrites customers.json and items.json files if they exist in the output directory.
-Ensure the input JSON file is correctly formatted to avoid processing errors.
   
     
