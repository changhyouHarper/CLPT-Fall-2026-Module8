# Module 8, Problem 2

# Define main() function
def main(): 

	# Declare an array to store 20 fibonacci display numbers 
	fibonacci_array = [1, 2, 3 ,4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

	# Declare variable to store first preceding number 
	first = 1

	# Declare variable to store second preceding number 
	second = 1 

	# Display the first and second numbers 
	print(first)
	print(second)

	# Create a for loop 
	# The first and second numbers have already been 
	# assigned and displayed. Start from the second 
	# index position until the end 
	for fibonacci in fibonacci_array[2:]:

		# Calculate the next number (first + second)
		next = first + second 

		# Display the sum in next 
		print(next)

		# Assign the second number to the first variable 
		first = second 

		# Assign the new number in next to the second variable 
		second = next

# Call main() function
if __name__ == "__main__":
	main()