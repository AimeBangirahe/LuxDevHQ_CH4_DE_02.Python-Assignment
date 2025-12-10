# Exercises
import math
import random
import time
import threading


# Use a for loop to print numbers from 1 to 10 - Done
def from_1_to_100():
	for i in range(100):
		print(i+1)
# from_1_to_100()

# Use a while loop to print numbers until the user enters stop.
stop = threading.Event()
def infinite_numbers():
	def printer():
		i = 1
		while not stop.is_set():
			print(i)
			i += 1
			time.sleep(1)
			
	threading.Thread(target=printer).start()
	
	while input().lower() != "stop": pass
	stop.set()
	print("Stopping...")
infinite_numbers()

# Write a loop that prints even numbers from 1 to 20.
def even_numbers():
	for i in range(1, 20):
		if i % 2 == 0:
			print('Even Number', i)
# even_numbers()

# Explain what break and continue do in your own words.
def break_continue():
	print("Break - Stops the loop immediately")
	print("Continue - Skip the current iterate and continues loop execution")
# break_continue()


# Challenge
# Write a guessing game that asks the user to guess a secret number between 1 and 10.
#
# Give feedback (too high / too low)
# Use a while loop

def guess_game():
	while True:
		secret_number = random.randint(1, 10)
		user_input = int(input('Enter number between 1 and 10:'))
		if user_input < secret_number:
			print('Too low of a guess try again, correct number', secret_number)
		elif user_input > secret_number:
			print("too high of a guess try again, correct number", secret_number)
		else:
			print('Guess is Correct Jackpot!', user_input, secret_number)
			break
# guess_game()