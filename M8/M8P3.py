# Module 8, Problem 3

# Define main() function
def main(): 

	# Declare variable to store sum of all bonus 
	bonus_total = 0

	# Open the text file, read the text file 
	# Keyword "with" will automatically close the .txt file 
	with open("M8P3.txt", "r") as file:

		# Read through the txt file line by line 
		employee_data = file.readlines()

		# Create a for loop to read employee information 
		for i in range(0, len(employee_data), 2):

			# Read employee last name + salary 
			last_name = employee_data[i].strip()
			salary = float(employee_data[i + 1].strip())

			# Calculate bonus rate 
			if (salary >= 100000):
				bonus = 0.20
			elif (salary >= 50000):
				bonus = 0.15
			else:
				bonus = 0.10

			# Calculate employee bonus 
			bonus = salary * bonus 

			# Accumulate bonus_total variable 
			bonus_total += bonus 

			# Display output back to user 
			print(f"\nEmployee: {last_name}")
			print(f"Salary: ${salary:,.2f}")
			print(f"Bonus: ${bonus:,.2f}")

	# Display total in bonuses paid 
	print(f"\nTotal Bonus Paid: ${bonus_total:,.2f}")

# Call main() function
if __name__ == "__main__":
    main()