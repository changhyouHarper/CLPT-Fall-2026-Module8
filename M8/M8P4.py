# Module 8, Problem 4

# Define main() function 
def main(): 

	# Define variable to store total of all items 
	item_total = 0

	# Define variable to store number of orders 
	order_count = 0 

	# Open and read the text file 
	with open("M8P4.txt", "r") as file:

		# Read M8P4.txt line by line 
		item_data = file.readlines()

		# Create a for loop to read through the item data 
		for i in range(0, len(item_data), 3):

			# Read item name, quantity, and price 
			item = item_data[i].strip()
			quantity = int(item_data[i + 1].strip())
			price = float(item_data[i + 2].strip())

			# Calculate the extended price
			extended_price = quantity * price 

			# Display item, quantity, price and extended price back to user
			print(f"\nItem: {item}")
			print(f"Quantity: {quantity}")
			print(f"Item Price: ${price:,.2f}")
			print(f"Extended Price: ${extended_price:,.2f}")

			# Accumulate the item_total variable 
			item_total += extended_price

			# Accumulate the order count 
			order_count += 1 

		# Calculate average 
		if order_count > 0:
			average_order = item_total / order_count

			# Display output back to user 
			print(f"\nTotal: ${item_total:,.2f}")
			print(f"Number of Orders: {order_count}")
			print(f"Average Order: ${average_order:,.2f}")

# Call main() function
if __name__ == "__main__":
    main()
