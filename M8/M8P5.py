# Module 8, Problem 5

# Define main() function
def main():

	# Declare variable to store cost_per_credit 
	cost_per_credit = 0 

	# Declare variable to store sum of all tuition owed 
	tuition_total = 0

	# Declare variable to store count (total number of students in .txt file read)
	count = 0 

	# Open and read the text file 
	# Keyword "with" will automatically close the file 
	with open("M8P5.txt", "r") as file:

		# Read M8P5.txt line by line 
		student_data = file.readlines()

		# Create a for loop to read through student_data
		for i in range(0, len(student_data), 3):

			# Read student last name, district code, credits taken 
			# and store in variable 
			last_name = student_data[i].strip()
			district_code = student_data[i + 1].strip()
			credits = int(student_data[i + 2].strip())

			# cost_per_credit varies depending if student
			# is in district or out of district 
			if (district_code == "I"):
				cost_per_credit = 250
			elif (district_code == "O"):
				cost_per_credit = 500

			# Declare variable to store / calculate tuition owed 
			tuition = credits * cost_per_credit

			# Display student last name, credits taken, tuition owed 
			print(f"\nStudent Last Name: {last_name}")
			print(f"Credits Taken: {credits}")
			print(f"Tuition: ${tuition:,.2f}")

			# Accumulate tuition total
			tuition_total += tuition 

			# Accumulate student count
			count += 1 

	# Display sum of tuition 
	print(f"\nTuition Total: ${tuition_total:,.2f}")
	print(f"Student Count: {count}")

# Call main() function
if __name__ == "__main__":
    main()


