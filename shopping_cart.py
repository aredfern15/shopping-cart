# shopping_cart.py

products = [
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


#
# INFO CAPTURE / INPUT
#


total_price = 0 
selected_ids = []

while True:
    selected_id = input("Please input a product identifier (1-20), or 'DONE' when finsihed: ") #> "9" (string)
    if selected_id == "DONE": 
        break 
    elif int(selected_id) <= 0 or int(selected_id) > 20:
        selected_id = input("Oops! The number selected is invalid. Please select a number between 1-20: ")
        selected_ids.append(selected_id)
    else: 
        selected_ids.append(selected_id)

print("---------------------------")
print("REDFERN GROCERY STORE")
print("---------------------------")
print("Web: www.redferngrocerystore.com")
print("Phone: 987-654-3210") 
print("Address: 123 Hoya Ln, Washington, D.C. 20057")

#Date and Time from https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import datetime  
    
# using now() to get current time  
now = datetime.now()
#print("now =", now)

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Check Date and Time:", dt_string) 
print("---------------------------")
#
# INFO DISPLAY / OUTPUT
#

#print(selected_ids)

for selected_id in selected_ids:  
        matching_products =  [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0] 
        total_price = total_price + matching_product["price"]
        print("SELECTED PRODUCT: " + matching_product["name"] + " " + str(matching_product["price"]))
print("---------------------------")

subtotal = str(total_price)
#print("SUBTOTAL: " + str(total_price)) #TODO Format as USD
print("SUBTOTAL: " + to_usd(float(subtotal)))
#Washington, DC has a sales tax of 6%
sales_tax = float(subtotal) * .06
print("SALES TAX (6%):", to_usd(sales_tax))
price_total = sales_tax + float(subtotal)
print("TOTAL: " + to_usd(price_total))
print("---------------------------")
print("THANK YOU FOR SHOPPING WITH US TODAY. WE LOOK FORWARD TO SEEING YOU AGAIN SOON!")
print("---------------------------")