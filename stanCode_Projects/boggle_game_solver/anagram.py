"""
File: anagram.py
Name: Amber Chang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""


# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variable
dictionary = {}


def main():
    read_dictionary()
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break
        else:
            find_anagrams(word)


def read_dictionary():
    dictionary_lst = []
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            dictionary_lst.append(word)

    for i in range(len(dictionary_lst)):
        # Create a dictionary with the first letter as the key
        if dictionary_lst[i][0] not in dictionary:
            dictionary[dictionary_lst[i][0]] = []
            dictionary[dictionary_lst[i][0]].append(dictionary_lst[i])
        else:
            dictionary[dictionary_lst[i][0]].append(dictionary_lst[i])


def find_anagrams(s):
    """
    :param s: The word that user inputs
    :return: The anagrams of that word
    """
    print('Searching...')
    anagrams = []
    letter_count = {}
    # This dictionary contains times of letters in the given word (s) appeared
    for letter in s:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    find_anagrams_helper(s, '', anagrams, letter_count)
    print(f'{len(anagrams)} anagrams: {anagrams}')


def find_anagrams_helper(s, current_str, anagrams, letter_count):
    if len(current_str) == len(s):
        if current_str == s or current_str in dictionary[current_str[0]]:
            # Base Case
            anagrams.append(current_str)
            print('Found: ', current_str)
            print('Searching...')
    else:
        for letter in letter_count:
            if letter_count[letter] > 0:
                current_str += letter
                letter_count[letter] -= 1
                # Choose

                if len(s) > len(current_str) > 1:
                    if has_prefix(current_str):
                        find_anagrams_helper(s, current_str, anagrams, letter_count)
                else:
                    find_anagrams_helper(s, current_str, anagrams, letter_count)
                    # Explore

                current_str = current_str[:len(current_str)-1]
                letter_count[letter] += 1
                # Un-choose


def has_prefix(sub_s):
    """
    :param sub_s: The substring of the possible anagram
    :return: Boolean, there are words in the dictionary containing the substring
    """
    for word in dictionary[sub_s[0]]:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()

