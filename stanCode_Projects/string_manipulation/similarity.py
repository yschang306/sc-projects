"""
File: similarity.py
Name: Amber Chang
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This program will find the most similar segment from the long
    DNA sequence by comparing the long DNA sequence with the short
    DNA sequence, all entered by users
    """
    s1 = input('Please give me a DNA sequence to search: ')
    # The long DNA sequence to be compared
    s2 = input('What DNA sequence would you like to match? ')
    # The short DNA sequence to match
    s1 = s1.upper()
    s2 = s2.upper()
    # Case-insensitive
    best_match = match(s1, s2)
    print('The best match is '+best_match)


def match(s1, s2):
    """
    :param s1: str, the long DNA sequence to be compared
    :param s2: str, the short DNA sequence to match
    :return: str, the most similar segment from the long DNA sequence
    """
    ans = ''
    maximum = 0
    # The maximum of match rate
    for i in range(len(s1) - len(s2) + 1):
        # (len(s1) - len(s2) + 1) is the times of matching
        match_rate = 0
        segment = s1[i: i+len(s2)]
        # The DNA segment from the long sequence to be compared
        for j in range(len(s2)):
            ch1 = segment[j]
            ch2 = s2[j]
            if ch1 == ch2:
                match_rate += 1 / len(s2)
        if maximum < match_rate:
            maximum = match_rate
            ans = segment
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
