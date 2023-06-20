# Golf Store Parser

This is a simple parser for retrieving data about products from a golf store. It utilizes the store's API and saves the retrieved data into JSON files for each product category.

## Project Description

The parser is designed to gather the following information about golf store products:

- Product name
- Price
- Description
- Photos
- Other specifications

## Installation and Usage

Follow the instructions below to install and use the parser:

1. Clone the repository to your local computer:
   ```shell
   git clone https://github.com/l-Spook-l/Golf-Store-Parser.git

2. Navigate to the project directory:
   ```shell
   cd golf-parser
   
3. Install the dependencies:
   ```shell
   pip install -r requirements.txt
   
4. Open the golf_parser.py file in your text editor.

5. In the categories dictionary, add or modify the product categories by providing their names, category IDs, and quantity of products:
   ```shell
   categories = {
    # Категория, id, количество товара
    'Golf clubs': ["0c8104f6-3b98-2b15-95cb-06f382d5a778", 99],
    'Clothing': ["7b716bef-d59a-7d97-36ee-994ad180e7d3", 99],
    'Shoes': ["5cdf8a7f-3347-97a2-21f9-192f6a9bc22f", 80],
    'Golf Bags': ["9e2c9222-0e43-7ffc-121a-0b7ccebbc554", 17],
    'Accessories': ["b93590b0-d8d0-6eae-31e5-ed5570f2615c", 60],
    'Balls': ["4839cba0-7843-3dc0-7ff2-9dcc64ff9e9f", 17],
   }

6. Run the parser:
   ```shell
   python main.py
   
7. Add the retrieved data to the database:
   ```shell
   python add_to_database.py

### Note:
If you encounter an error when running the parser, try replacing the value of the Authorization header with your own.

### Copying the Authorization Header
To copy the value of the Authorization header from your browser, you will need a browser developer tool. Here are instructions for several popular browsers:

# Google Chrome:
1. Open the webpage for which you need to copy the Authorization header.
2. Right-click on the page and select "Inspect" or "Inspect Element". This will open the developer tools panel.
3. In the developer tools panel, find the "Network" tab and switch to it.
4. Refresh the page to activate the recording of network requests.
5. Find the relevant request in the request list. If there are many requests, you can use search or filters to locate the desired one.
6. Click on the request to open its details.
7. In the "Headers" section, find the Authorization header. Right-click on it and select "Copy value" or a similar command.

# Mozilla Firefox:
1. Open the webpage for which you need to copy the Authorization header.
2. Right-click on the page and select "Inspect Element" or "Inspect". This will open the developer tools panel.
3. In the developer tools panel, find the "Network" tab and switch to it.
4. Refresh the page to activate the recording of network requests.
5. Find the relevant request in the request list. If there are many requests, you can use search or filters to locate the desired one.
6. lick on the request to open its details.
7. In the "Headers" section, find the Authorization header. Right-click on it and select "Copy value" or a similar command.

# Internet Explorer:
1. Open the webpage for which you need to copy the Authorization header.
2. Right-click on the page and select "Inspect Element" or "Inspect". This will open the developer tools panel.
3. In the developer tools panel, find the "Network" tab and switch to it.
4. Refresh the page to activate the recording of network requests.
5. Find the relevant request in the request list. If there are many requests, you can use search or filters to locate the desired one.
6. Click on the request to open its details.
7. In the "Headers" section, find the Authorization header. Right-click on it and select "Copy" or a similar command.