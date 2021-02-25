# shopping-cart
Shopping Cart Exercise 

** README.md file assisted, guided, and copied by Professor Rossetti's example in the class Shopping Cart Exercise **

# Instructions
In the Shopping Cart Exercise, we will develop a Python application that will help grocery store employees do their job while fulfilling the requests of the store owner. 

Before starting the actual exercise, we need to download, setup and run the application. 

First, we need to go to GitHub and follow the "Setup" instructions below. After completing that step, we need to make a local copy on your own computer to develop. 

Remember to use the command-line or GitHub Desktop to "commit", or save new versions of, your code. And remember to "push" to your remote project repository on GitHub at least once before you're done.

# Setup

# Repo Setup 

To setup, use GitHub to create a new remote project repository called  "shopping-cart". After naming the repository, name the "README.md" file and a Python-flavored ".gitignore" file during the repo creation process. After this process is complete, you should be able to view the repo on GitHub. 

After creating the remote repo, use GitHub Desktop to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:
cd ~/Desktop/shopping-cart

Use your text editor or the command-line to create a file in that repo called "shopping_cart.py", and then place the following contents inside:

    ## shopping_cart.py

##products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


    ## TODO: write some Python code here to produce the desired output

print(products)

Remember to save your files to ensure that the contents remain in the file. After setting up a virtual environment, we will be ready to run this file.

# Enviornment Setup 

You will not need to use any third-party packages for this project. However, if you desire to complete the extra credit, you will eventually need to use the "base" Anaconda environment. Afterwards, you'll want to create and activate a new Anaconda virtual environment, and use a "requirements.txt" file approach to installing your packages (such as pip):

    ## IF USING THIRD-PARTY PACKAGES, USE A NEW ENV:
conda create -n shopping-env python=3.8 
conda activate shopping-env
pip install -r requirements.txt # (after specifying desired packages inside)
Within an active virtual environment of choice ("base" or project-specific), demonstrate your ability to run the Python script from the command-line:

python shopping_cart.py

If you see the provided "products" data structure, you're ready to move on to project development. If this works, then make your first commit, with a message like "Setup the repo".

# Data Setup

The provided code includes a variable called "products" which facilitates management of the products inventory from within the application's source code.

# Info Input 

We want to set up the project first inputting the information needed to scan and record the products purchased. As seen above, the information for products and the USD have been placed in your file already as a starting point. 

Now, we need to create product identifiers that will allow people to know what they have purchased. Also, we need to prepare for invalid inputs (those that do not fall under the provided products list) and a system that allows people to say "DONE" after that have scanned the appropriate products. Be sure to identify the selected products in your cart. HINT: You want to use  "while True", "if" and "else" to guide you. 


# Info Outputs 

After successfully scanning the products, we need to finish the products by producing a receipt that displays store infromation (store name, phone number, store address), displays the current checkout date and time, displays the names and prices of all the scanned products, and displays tax and totals. HINT: for finding the date and time, reference https://www.geeksforgeeks.org/get-current-date-and-time-using-python/. When solving for the tax, reference the "usd" notes that you first downloaded above.


After you do that, the preliminary project is finished. You can now either turn in the project via Gia repository which reflects an incremental history or begin to try the extra credit bonus. 