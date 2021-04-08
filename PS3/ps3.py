# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    word = word.lower()
    wordcopy = word
    first_component = 0
    second_component = 1

    if '*' in wordcopy:
        for vowel in VOWELS:
            wordcopy = wordcopy.replace("*", vowel)
            if wordcopy in word_list:
                word = wordcopy
                break
            else:
                wordcopy = word

    for c in word:
        first_component += SCRABBLE_LETTER_VALUES[c]

    if 7 * len(word) - 3 * (n - len(word)) > 1:
        second_component = 7 * len(word) - 3 * (n - len(word))

    return (first_component * second_component)

    
#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print("")                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    hand["*"] = 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    word = word.lower()
    update = hand.copy()

    for letter in word:
        if letter in update.keys():
            update[letter] -= 1


    for key in hand.keys():
        if update[key] < 1:
            update.pop(key)

    return update

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    word = word.lower()
    wordcopy = word

    if not(hand_word_tally(word, hand)):
            return False

    if '*' in wordcopy:
        for vowel in VOWELS:
            wordcopy = wordcopy.replace("*", vowel)
            if wordcopy in word_list:
                word = wordcopy
                return True
            else:
                wordcopy = word

        return False
    else:
        if word not in word_list:
            return False
        else:
            return True

def hand_word_tally(word, hand):
    hand_copy = hand.copy()
    for letter in word:
            if letter in hand_copy.keys():
                hand_copy[letter] -= 1
                if hand_copy[letter] < 0:
                    return False
            else:
                return False
    
    return True

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    return len(hand)

def play_hand(hand, word_list):
    total_score = 0
    substitute_signal = True
    while calculate_handlen(hand):
        print("Current hand : ", end="")
        display_hand(hand)

        if substitute_signal:
            substitute_signal = False
            answer = input("Would you like to substitute a letter? ")
            if answer.lower() == "yes":
                letter = input("Which letter would you like to replace: ")
                hand = substitute_hand(hand, letter)
                print("------------")
                continue
            else:
                print("------------")
                continue 

        word = input("Enter word, or !! to indicate that you are finished: ")
        if word == "!!":
            print("Total score for this hand:", total_score)
            return total_score

        if is_valid_word(word, hand, word_list):
            hand = update_hand(hand, word)
        else:
            print("That is not a valid word. Please choose another word.")
            print("------------")
            continue

        
        
        total_score += get_word_score(word, calculate_handlen(hand))
        print(word, " earned ", get_word_score(word, calculate_handlen(hand))," points.", end="")
        print(" Total : ", total_score)
    
    print("Ran out of letters.\nTotal score for this hand: ", total_score)
    
    return total_score



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    all_words = VOWELS + CONSONANTS
    x = random.choice(all_words)
    while x not in hand:
        x = random.choice(all_words)

    hand[x] = hand[letter]
    del hand[letter]
    return hand

       
    
def play_game(word_list):
    grand_total = 0
    current_hand_score = 0
    replay_signal = True
    hands = int(input("Enter total number of hands: "))
    while hands:
        current_hand = deal_hand(HAND_SIZE)
        current_hand_score = play_hand(current_hand, word_list)
        print("--------------")
        hands -= 1
        if replay_signal and hands > 0:
            answer = input("Would you like to replay the hand? ")
            if answer.lower() == "yes":
                replay_signal = False
                current_hand_score = play_hand(current_hand, word_list)
        grand_total += current_hand_score
    print("Total score over all hands: ", grand_total)
    
        
        
        



    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
