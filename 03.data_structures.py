# Create a list of 5 fruits and print the third fruit. - Done
def fruit_list():
	l1 = ['apple', 'pineapple', 'mango', 'banana', 'peach']
	print(l1[2])

# Create a dictionary with keys: name, age. Print the value of age. - Done
def dictionary():
	d1 = {'name': 'Aineah', 'Age': '27'}
	print(d1['Age'])

# Define a tuple with three numbers. Try modifying it. What happens? - Done
def tuple_():
	t1 = (1, 2, 3)
	print(t1, type(t1))
	print('Tuples are immutable')

# Create a set from a list with duplicate values. - Done.
def set_list():
	l1 = ['apple', 'pineapple', 'mango', 'banana', 'peach', 'mango', 'apple']
	s1 = set(l1)
	print(s1)
	print('set removes duplicates')

# Challenge
# Create a program that:
#
# Takes 5 user inputs and stores them in a list - Done
# Converts the list into a set and prints the unique values - Done

def dup_remove():
	# used List Compression
	max_input_range = 5
	numbers = [input(f"Enter number {i+1}: ") for i in range(max_input_range)]
	print("Unique values:", list(set(numbers)))

fruit_list()
dictionary()
tuple_()
set_list()
dup_remove()

