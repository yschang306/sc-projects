"""
File: boggle.py
Name: Amber Chang
----------------------------------------
This program demonstrates the Boggle game.
It recursively finds all words that are on
the Boggle word board input by user.
"""


# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# Global variable
dictionary_lst = []
# This list contains all words in the file dictionary.txt
dictionary = {}
# This dictionary classifies the dictionary list above by using every alphabet as key


def main():
	"""
	This program finds all words that are on the Boggle word
	board as user inputs letters on every rows.
	"""
	read_dictionary()
	create_dictionary()
	all_letters = []
	# This list contains all letters that user input
	for i in range(4):
		letters = input(f'{i+1} row of letters: ')
		letters = letters.lower()
		# Case-insensitive
		if not check_format(letters):
			print('Illegal input')
			break
		else:
			all_letters.append(letters.split())
			# Adding letters by row, meaning letters of each row is another list in the all_letter list
	if len(all_letters) == 4:
		words_lst = find_words(all_letters)
		print('There are', len(words_lst), 'words in total.')


def check_format(letters):
	"""
	This function checks whether the string that user inputs
	meets the format, e.g. 'a b c d', every alphabet should have
	a blank space between it.
	------------------------------------------------------------
	:param letters: (str) Letters input by user
	:return: (bool) Whether it meets the format
	"""
	if len(letters.split()) == 4:
		for letter in letters.split():
			if letter not in dictionary:
				return False
		return True
	return False


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			dictionary_lst.append(word)


def create_dictionary():
	"""
	This function creates a dictionary with each alphabet as the key.
	"""
	for i in range(len(dictionary_lst)):
		if dictionary_lst[i][0] not in dictionary:
			dictionary[dictionary_lst[i][0]] = []
			dictionary[dictionary_lst[i][0]].append(dictionary_lst[i])
		else:
			dictionary[dictionary_lst[i][0]].append(dictionary_lst[i])


def find_words(letters_lst):
	"""
	:param letters_lst: (lst) All letters that user inputs
	:return words_lst: (lst) All words that are found
	"""

	words_lst = []
	# This list contains all words that are found
	index_track = []
	# This tracks all the letters that has been used by recording tuples of indexes, e.g. (row, column)

	for i in range(4):
		# i is the current row
		for j in range(4):
			# j is the current column
			letter = letters_lst[i][j]
			# The first letter of a word to search its neighbor letter
			index_track.append((i, j))
			find_words_helper(letters_lst, letter, words_lst, i, j, index_track)
			index_track.pop()

	return words_lst


def find_words_helper(letters_lst, current_str, words_lst, current_row, current_column, index_track):

	if len(current_str) >= 4:
		sub_dictionary = find_same_prefix(current_str)
		# This dictionary contains words that share the same prefix
		# Only when the length of current word is greater or equal to 4, it will start to search
	else:
		sub_dictionary = []

	if len(sub_dictionary) == 1 and current_str in sub_dictionary:
		# Base case
		if current_str not in words_lst:
			words_lst.append(current_str)
			print(f'Found "{current_str}"')

	else:
		if len(sub_dictionary) > 1:
			# There are longer words based on the current word
			if current_str in sub_dictionary:
				if current_str not in words_lst:
					words_lst.append(current_str)
					print(f'Found "{current_str}"')

		for i in range(-1, 2):
			neighbor_row = current_row + i
			for j in range(-1, 2):
				neighbor_column = current_column + j
				if 4 > neighbor_row >= 0 and 4 > neighbor_column >= 0:
					if (neighbor_row, neighbor_column) not in index_track:
						current_str += letters_lst[neighbor_row][neighbor_column]
						index_track.append((neighbor_row, neighbor_column))
						# Choose

						if has_prefix(current_str):
							find_words_helper(letters_lst, current_str, words_lst, neighbor_row, neighbor_column, index_track)
							# Explore

						current_str = current_str[:len(current_str)-1]
						index_track.pop()
						# Un-choose


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary[sub_s[0]]:
		if word.startswith(sub_s):
			return True
	return False


def find_same_prefix(current_str):
	"""
	:param: current_str: (str) The current string that is constructed by neighboring letters on a 4x4 square grid
	:return: sub_dictionary: (lst) Words that share the same prefix
	"""
	sub_dictionary = []
	for word in dictionary[current_str[0]]:
		if word.startswith(current_str):
			sub_dictionary.append(word)
	return sub_dictionary


if __name__ == '__main__':
	main()
