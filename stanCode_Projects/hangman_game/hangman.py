"""
File: hangman.py
Name: Amber Chang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program will display the hangman game. When users
    enter a letter, it will identify whether the letter is
    in the answer. If the letter is in the answer, it shows
    that part of the word; otherwise, users lose one chance.
    """
    answer = random_word()
    dashed_word = dashed(answer)
    print('The word looks like: '+dashed_word)
    print('You have '+str(N_TURNS)+' guesses left.')
    letter = input('Your guess: ')
    letter = letter.upper()
    # Case-insensitive
    guess(letter, answer, dashed_word)


def reveal(ch, answer):
    """
    This function will reveal the positions of the letter that
    is in the answer.
    :param ch: str, the characters that are in the answer
    :param answer: str, the word to be guessed
    :return: str, the revealed word after each guessing
    """
    ans = ''
    for i in range(len(answer)):
        for base in ch:
            if answer[i] == base:
                ans += base
        if len(ans) == i:
            ans += '_'
            # if the letter is not in the answer, it shows '_'
    return ans


def guess(letter, answer, dashed_word):
    """
    This function will identify whether the letter is in the answer
    and give the response accordingly. Then, it will end the process
    until users have the correct answer or run out of their chances.
    :param letter: str, the letter that users enter
    :param answer: str, the word to be guessed
    :param dashed_word: str, the dashed answer showing in the beginning
    """
    turns_left = N_TURNS
    after = dashed_word
    # The revealed word after guessing
    ch = ''
    # Character that is in the answer
    while True:
        if letter.isalpha() and len(letter) == 1:
            if letter in answer:
                print('You are correct!')
                if letter not in ch:
                    ch += letter
                after = reveal(ch, answer)
                if after == answer:
                    print('You win!!')
                    print('The word was: '+answer)
                    break
                else:
                    print('The word looks like: ' + after)
                    print('You have ' + str(turns_left) + ' guesses left.')
            else:
                print('There is no ' + letter + '\'s in the word.')
                turns_left -= 1
                if turns_left == 0:
                    print('You are completely hung : (')
                    print('The word was: '+answer)
                    break
                else:
                    print('The word looks like: ' + after)
                    print('You have ' + str(turns_left) + ' guesses left.')
        else:
            print('illegal format.')
        letter = input('Your guess: ')
        letter = letter.upper()
        # Case-insensitive


def dashed(answer):
    """
    This function will show the dashed answer
    :param answer: str, the word to be guessed
    :return: str, the dashed answer
    """
    ans = ''
    for i in range(len(answer)):
        ans += '_'
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
