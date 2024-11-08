
🛍️ Tech Equipment Store - Inventory and Ordering System

This project is a Python-based inventory management and ordering system for a tech equipment store (like “Best Buy”). The application allows users to list available products, check stock levels, and place orders for multiple products at once.

🚀 Features

	•	Product Management: Each product is represented by the Product class, which tracks the name, price, available quantity, and whether the product is active.
	•	Store Management: The Store class manages a collection of products, providing functionality to:
	•	Add and remove products from inventory
	•	Display all active products in stock
	•	Process customer orders and update stock levels
	•	User Interface: The command-line interface allows users to:
	1.	List all products available in the store
	2.	Show the total amount of all products in the store
	3.	Make an order by selecting products and quantities
	4.	Exit the program

📂 Project Structure

.
├── products.py          # Product class definition
├── store.py             # Store class definition for managing inventory
├── main.py              # test_main() for products.py
|---main_ui.py           # main function for store with user_interface and main logic
|---main_2.py            # test_main() for store.py
|---user_interface.py    # User interface
├── README.md            # Project documentation
└── requirements.txt     # (Optional) Dependencies file, if needed

🛠️ Installation and Setup

	1.	Clone the Repository:

git clone https://github.com/your-username/your-repo.git
cd your-repo


	2.	Install Dependencies (if any are used):
If there are any external dependencies, list them in a requirements.txt file, then install using:

pip install -r requirements.txt


	3.	Run the Program:
Start the program by running the main_ui.py file:

python main_ui.py



📝 How to Use

Upon running the program, you will be presented with a menu to interact with the store:
	1.	List all products in store: Shows all active products and their details (name, price, and quantity).
	2.	Show total amount in store: Displays the total quantity of all items currently in stock.
	3.	Make an order: Allows you to select products, specify quantities, and calculate the total price of your order.
	4.	Quit: Exit the program.

Example

Here’s a sample interaction with the program:

Please enter your choice (1-4):
1
Available products:
1. MacBook Air M2, Price: 1450, Quantity: 100
2. Bose QuietComfort Earbuds, Price: 250, Quantity: 500
3. Google Pixel 7, Price: 500, Quantity: 250

Please enter your choice (1-4):
3
Available products:
1. MacBook Air M2, Price: 1450, Quantity: 100
2. Bose QuietComfort Earbuds, Price: 250, Quantity: 500
3. Google Pixel 7, Price: 500, Quantity: 250

Enter the number of the product you want to buy (or 0 to stop): 1
How many units of MacBook Air M2 do you want to buy? 2

Enter the number of the product you want to buy (or 0 to stop): 0
Order placed successfully! Total price: 2900 dollars

✨ Product and Store Classes Overview

Product Class

	•	Attributes:
	•	name: Product name (string)
	•	price: Product price (float)
	•	quantity: Product quantity available (int)
	•	active: Status of the product (bool)
	•	Methods:
	•	get_quantity(): Returns the product quantity.
	•	set_quantity(): Updates the quantity and deactivates the product if quantity is 0.
	•	is_active(): Returns whether the product is still active.
	•	buy(): Processes a purchase, updating the stock and returning the total price.

Store Class

	•	Attributes:
	•	products: A list of Product instances.
	•	Methods:
	•	add_product(): Adds a product to the store.
	•	remove_product(): Removes a product from the store.
	•	get_total_quantity(): Returns the total quantity of all products in the store.
	•	get_all_products(): Returns a list of active products in the store.
	•	order(): Processes an order of multiple products, adjusting quantities and calculating the total price.

🛡️ Error Handling

The program includes error handling for various situations:
	•	If an invalid product number is entered, the program will prompt the user to try again.
	•	If an order is placed with a quantity that exceeds the available stock, an exception is raised.

🤝 Contributions

Contributions are welcome! If you’d like to add new features, fix bugs, or improve the documentation, feel free to fork the repository and submit a pull request.

📜 License

This project is open source and available under the MIT License.