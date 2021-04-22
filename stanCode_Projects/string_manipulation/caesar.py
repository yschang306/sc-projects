"""
File: caesar.py
Name: Amber Chang
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program will decipher the ciphered string as users input
    the secret number
    """
    n = int(input('Secret number: '))
    new_alphabet = cipher(n)
    str1 = input("What's the ciphered string? ")
    str1 = str1.upper()
    # Case-insensitive
    new_str = decipher(str1, new_alphabet)
    print('The deciphered string is: '+new_str)


def decipher(str1, new_alphabet):
    """
    :param str1: str, the ciphered string, which users input
    :param new_alphabet: str, the ciphered alphabet
    :return: str, the deciphered string
    """
    ans = ''
    for base in str1:
        if base.isalpha():
            i = new_alphabet.find(base)
            ans += ALPHABET[i]
        else:
            ans += base
    return ans


def cipher(n):
    """
    :param n: int, the secret number, which users input
    :return: str, the ciphered alphabet
    """
    ans = ''
    for i in range(n):
        ans += ALPHABET[26 - n + i]
    for j in range(n, len(ALPHABET)):
        ans += ALPHABET[j - n]
    return ans


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
