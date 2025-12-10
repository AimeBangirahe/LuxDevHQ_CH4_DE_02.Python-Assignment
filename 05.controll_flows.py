# Exercises

# Write a program that checks if a number is positive, negative, or zero.
def number_check():
	user_input = int(input('Enter number to check: '))

	if user_input < 0:
		print('Negative Number', user_input)
	elif user_input > 0:
		print('Positive Number', user_input)
	elif user_input == 0:
		print('Zero Number', user_input)
	else:
		print('Invalid Number')
# number_check()

# Create a program that checks if someone is eligible to vote.
def voter_check():
	age = int(input('Enter your age: '))
	if age > 18:
		print('Eligible to Vote')
	else:
		print('Too young to vote')
# voter_check()

# Write a program that takes 3 numbers and prints the largest one.
def large_number():
	nums = [int(input(f"Enter number {i+1}: ")) for i in range(3)]
	print("Largest number is", max(nums))
# large_number()

# Practice combining and, or, not.
def and_not_or():
	age = int(input("Enter your age: "))
	has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"
	
	if age >= 18 and has_id:
		print("You are allowed in.")
	elif age >= 18 and not has_id:
		print("You must bring your ID.")
	elif age < 18 or not has_id:
		print("You are not allowed in.")
	else:
		print("Condition not clear.")
# and_not_or()

# Challenge
# Build a grading system:
#
# Input score (0–100)
# Output grade: A (90+), B (80–89), etc.
def grading():
	score = int(input('Enter score acquired: '))
	if score > 90:
		print('Grade A')
	elif 89 >= score >= 80:
		print("Grade B")
	elif 79>= score >= 70:
		print("Grade C")
	elif 69>= score >= 60:
		print('Grade D')
	elif 59>= score >= 50:
		print("Grade E")
	else:
		print("Failed!")
grading()



