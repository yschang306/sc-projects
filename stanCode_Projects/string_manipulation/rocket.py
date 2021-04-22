"""
File: rocket.py
Name: Amber Chang
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	This program will draw a rocket based on
	the value of the constant - SIZE.
	"""
	head()
	belt()
	upper_body()
	lower_body()
	belt()
	head()


def lower_body():
	"""
	This function will build the lower body of the rocket
	"""
	for i in range(SIZE):
		for j in range(2 * SIZE + 2):
			if j == 0 or j == 2 * SIZE + 1:
				print('|', end="")
			elif j - i <= 0:
				print('.', end="")
			elif i + j >= 2 * SIZE + 1:
				print('.', end="")
			elif (i + j) % 2 == 1:
				print('\\', end="")
			else:
				print('/', end="")
		print('')


def upper_body():
	"""
	This function will build the upper body of the rocket
	"""
	for i in range(SIZE):
		for j in range(2 * SIZE + 2):
			if j == 0 or j == 2 * SIZE + 1:
				print('|', end="")
			elif i + j < SIZE:
				print('.', end="")
			elif j - i > (SIZE + 1):
				print('.', end="")
			elif SIZE % 2 == 1:
				if (i + j) % 2 == 1:
					print('/', end="")
				else:
					print('\\', end="")
			elif (i + j) % 2 == 1:
				print('\\', end="")
			else:
				print('/', end="")
		print('')


def belt():
	"""
	This function will build the belt of the rocket
	"""
	for i in range(2 * SIZE + 2):
		if i == 0 or i == 2 * SIZE + 1:
			print('+', end="")
		else:
			print('=', end="")
	print('')


def head():
	"""
	This function will build the head of the rocket
	"""
	for i in range(SIZE):
		for j in range(2 * SIZE + 2):
			if j <= SIZE:
				if i + j < SIZE:
					print(' ', end="")
				else:
					print('/', end="")
			elif j - i > (SIZE + 1):
				print(' ', end="")
			else:
				print('\\', end="")
		print('')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()