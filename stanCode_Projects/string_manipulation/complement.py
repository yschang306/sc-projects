"""
File: complement.py
Name: Amber Chang
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
The program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This program will find the complement strand of
    a DNA sequence, inputted by users.
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement: ')
    dna = dna.upper()
    # Case-insensitive
    new_dna = build_complement(dna)
    print('The complement of '+dna+' is '+new_dna)


def build_complement(dna):
    """
    :param dna: str, the DNA sequence to be converted
    :return: str, the complement strand of the DNA sequence
    """
    ans = ''
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'C':
            ans += 'G'
        elif base == 'G':
            ans += 'C'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
