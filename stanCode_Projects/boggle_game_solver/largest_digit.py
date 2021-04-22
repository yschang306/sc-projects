"""
File: largest_digit.py
Name: Amber Chang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: The integer that is given
	:return: The largest digit of the integer
	"""
	if n < 0:
		n = -n
	if 0 < n < 10:
		# Base case
		return n
	else:
		if n % 10 > n // 10 % 10:
			# n % 10 is the first digit counted from right side of the integer
			# n // 10 % 10 is the second digit counted from right side of the integer
			return find_largest_digit(n//10 + (n % 10 - n // 10 % 10))
			# n // 10 is to reduce the number of digits from right side
			# (n % 10 - n // 10 % 10) is the difference between the two number
			# Adding the difference to keep the larger digit in the integer
		else:
			return find_largest_digit(n // 10)


if __name__ == '__main__':
	main()
