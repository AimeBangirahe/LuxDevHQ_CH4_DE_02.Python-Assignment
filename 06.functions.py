# Exercises


# Write a function greet(name) that prints “Hello, [name]”.
def greet(name: str):
	print(f'Hello {name}')
# greet("Aineah")

# Create a function add(a, b) that returns the sum.
def sum_num():
	num1 = int(input("Enter number 1: "))
	num2 = int(input("Enter number 2: "))
	
	print('Sum is:', num1 + num2)
	return num1 + num2
# sum_num()

# Modify add() to print “even” or “odd” based on the result.
# Call a function from within another function.
def add():
	number = sum_num()
	if number % 2 == 0:
		print('Even')
	else:
		print('Odd')
# add()

# Challenge
# Write a calculator function:
#
# Takes two numbers and an operation (+, -, *, /)
# Returns the result

def calculator():
	num1 = int(input('Enter number 1: '))
	num2 = int(input('Enter number 2: '))
	operator = input('Enter operator (+, -, *, /): ')
	
	if operator == '+':
		print('Ans =', num1 + num2)
	elif operator == '-':
		print("Ans =", num1 - num2)
	elif operator == '*':
		print('Ans =', num1 * num2)
	else:
		print('Ans =',  num1 / num2)
		
calculator()
	
