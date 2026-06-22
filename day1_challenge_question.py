# Make a complete small program called My First Python Bill Maker.

# Your program should:

# Ask the customer name
# Ask the item name
# Ask the item price
# Ask the quantity
# Calculate the total bill
# Print a clean bill
cust_name=input("what is your name")
item_name=input("tell me item name")
item_price=int(input("what is the price of item"))
quantity=int(input("how many you want?"))
print("Calculating  the total bill....")
bill=item_price*quantity

print("hello ",cust_name)
print("total bill for ",item_name,"is",bill)