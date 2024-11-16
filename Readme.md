

Best Buy Tech Store

Welcome to the Best Buy Tech Store! This is a console-based store management system where users can browse products, check inventory, and place orders. The system also supports special promotions and validates product properties, such as price and quantity. Additionally, the program tests several Python magic methods to enhance functionality, such as comparison operations and product validation.

Table of Contents

	•	Features
	•	Requirements
	•	Installation
	•	How to Run
	•	Usage
	•	Testing Magic Methods
	•	File Structure
	•	Contributing
	•	License

Features

	•	List products: Displays all available products in the store.
	•	Promotions: Some products have promotions like “30% off” or “Buy 2, Get 1 Free.”
	•	Order system: Users can select products and quantities to place an order.
	•	Inventory management: Supports different types of products such as standard, limited-stock, and non-stocked items.
	•	Magic Methods Testing: Tests Python’s special methods for comparison and other functionality.
	•	Error handling: Validates product properties (e.g., price cannot be negative).
	•	Interactive CLI: Simple and intuitive command-line interface for user interaction.

Requirements

To run this project, you need to have the following installed:
	•	Python 3.8 or above

Installation

	1.	Clone the repository to your local machine:

git clone https://github.com/your-username/Best_Buy.git
cd best-buy-tech-store


	2.	(Optional) Set up a virtual environment to isolate dependencies:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


	3.	Install required dependencies:

pip install -r requirements.txt



How to Run

To start the application, run the main_ui.py file:

python3 main_ui.py

This will launch the store’s main menu. You can then select one of the following options:
	1.	List all products in store: Displays the current inventory.
	2.	Show total amount in store: Shows the total quantity of all products.
	3.	Make an order: Allows you to select products and quantities to place an order.
	4.	Quit: Exits the program.

Usage

When you run the program, the following menu will be displayed:

Welcome to Best Buy Tech Store!
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit

Sample Interaction:

	1.	List Products:

MacBook Air M2, Price: $1450, Quantity: 100
Bose QuietComfort Earbuds, Price: $250, Quantity: 500


	2.	Make an Order:
	•	You can select the product number and quantity to add to your shopping list.
	•	When the order is complete, the total price is displayed, and the store inventory is updated.

Promotions:

Some products may have promotions applied, such as:
	•	Second Half Price: Buy two items, and the second one is 50% off.
	•	Third One Free: Buy two items, and the third one is free.
	•	Percent Discount: A percentage off on certain products (e.g., 30%).

Testing Magic Methods

The program also includes functionality to test several Python magic methods like:
	•	Comparison (>): Compare products based on their prices.
	•	Contains (in): Check if a product is available in the store.
	•	Property Validation: Raises an error if an invalid price is set.

To test these methods, you can inspect the main_ui.py file, which performs tests like:

print(mac > bose)  # True, since MacBook Air M2 is more expensive than Bose earbuds
print(mac in best_buy)  # True, since MacBook Air M2 is in the store's inventory

File Structure

├── promotions.py        # Handles the promotion logic for products
├── products_2.py        # Defines the Product classes (Products, LimitedProduct, NonStockedProduct)
├── store_2.py           # Store class, manages inventory and orders
├── user_interface.py    # The main user interface for interacting with the store
├── main_ui.py           # The main entry point to run the program
├── README.md            # This readme file
└── requirements.txt     # List of dependencies (if any)

Contributing

If you’d like to contribute to the project, feel free to submit pull requests or report issues. Any contributions are greatly appreciated!
	1.	Fork the repository
	2.	Create a new branch: git checkout -b feature-branch
	3.	Commit your changes: git commit -m 'Add new feature'
	4.	Push to the branch: git push origin feature-branch
	5.	Open a pull request

License

This project is licensed under the MIT License - see the LICENSE file for details.

