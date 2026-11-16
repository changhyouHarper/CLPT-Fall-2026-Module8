# Module 8, Problem 1 

# Define main() function 
def main(): 

	# Declare an array to store number of years we'll iterate through 
	year_range = [1, 2, 3, 4, 5]

	# Declare variable to store annual interest 
	interest_earned = 0

	# Declare variable to store total interest earned
	accumulated_interest = 0

	# Declare variable to store ending balance 
	ending_balance = 0

	# Prompt the user to enter a principal amount 
	beginning_balance = float(input("Enter principal amount: $"))

	# Prompt the user to enter the interest rate
	interest_rate = float(input("Enter the interest rate: "))

	print("\nYear\tBeginning Balance\tEnding Balance")

	# Create a for loop 
	for year in year_range:

		# Calculate annual interest
		interest_earned = beginning_balance * interest_rate

		# Calculate ending balance 
		ending_balance = beginning_balance + interest_earned

		# Accumulate total interest earned 
		accumulated_interest += interest_earned

		# Display output back to user 
		print(f"{year}\t${beginning_balance:,.2f}\t\t${ending_balance:,.2f}")

		# Update amount for next year balance 
		beginning_balance = ending_balance

	print(f"\nTotal interested earned: ${accumulated_interest:,.2f}")

# Call main() function
if __name__ == "__main__":
	main()