# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
  """Going over each letter of secret_word.
  If any letter is not in letters_guessed, False is returned.
  Otherwise returning true at the end."""

  for c in secret_word:
    if c not in letters_guessed:
      return False
  return True


def get_guessed_word(secret_word, letters_guessed):
  word = "" #Initializing a blank string
  for c in secret_word:
    if c in letters_guessed:
      word += c
    else:
      word += "_ "
      
  return word



def get_available_letters(letters_guessed):
  """String all has all the letters in it and word is empty.
  We iterate over all and add each letter which is not in
  letters_guessed to word"""
  all = "abcdefghijklmnopqrstuvwxyz"
  word = ""
  for c in all:
    if c not in letters_guessed:
      word += c

  return word
    
    

def hangman(secret_word):
  guesses_left = 6
  warnings_left = 3
  word = secret_word
  letters_guessed = ""
  loss_signal = True

  print("Welcome to the game Hangman!")
  print("I am thinking of a word that is ", len(word)," letters long.")
  print("You have ", warnings_left, " left.")
  print("---------------------------------------")

  while guesses_left:
    if is_word_guessed(word, letters_guessed):
      print("Congratulations, you won!")
      print("Your total score for this game is: ", (guesses_left * (26 - len(get_available_letters(word)))))
      loss_signal = False
      break

    print("You have ", guesses_left," left.")
    print("Available letters : ",get_available_letters(letters_guessed))
    letter = input("Please guess a letter :").lower()
    
    if is_word_guessed(letter, letters_guessed):
      warnings_left -= 1
      print("Oops! You've already guessed that letter. ", end="")

      if warnings_left != 0:
        print("You have ", warnings_left, " warnings left : ", get_guessed_word(word, (letters_guessed + letter)))
      else:
        guesses_left -= 1
        print("You have no warnings left, so you lose one guess. : ", get_guessed_word(word, (letters_guessed + letter)))

    elif not(letter.isalpha()):
      warnings_left -= 1
      print("Oops! That is not a valid letter. ", end="")

      if warnings_left != 0:
        print("You have ", warnings_left," warnings left: ",get_guessed_word(word, (letters_guessed + letter)))
      else:
        guesses_left -= 1
        print("You have no warnings left, so you lose one guess. : ", get_guessed_word(word, (letters_guessed + letter)))

    elif len(letter) == 1:
      if is_word_guessed(letter, word):
        print("Good guess: ", get_guessed_word(word, (letters_guessed + letter)))
      else:
        guesses_left -= 1
        print("Oops! That letter is not in my word: ", get_guessed_word(word, (letters_guessed + letter)))

    letters_guessed += letter
    print("---------------------------------------\n")

  if loss_signal:
    print("Sorry, you ran out of guesses. The word was ", word,".")

    
    






# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
  #Second part checks if each of the guessed letter matches the word's letter or not.
  c = 0
  i = 0
  while c < len(my_word):
    if my_word[c] == '_':
      c += 2
      i += 1
      continue
    if other_word[i] != my_word[c]:
      return False
    c += 1
    i += 1

  return True


def show_possible_matches(my_word):
  count = 0
  for r in range(len(my_word)):
    if my_word[r] == '_':
      count += 1

  length = len(my_word) - count
  print("Possible word matches are: ")
  for word in wordlist:
    if length == len(word): 
      if match_with_gaps(my_word, word):
        print(word+" ", end="")
  print("")



def hangman_with_hints(secret_word):
  guesses_left = 6
  warnings_left = 3
  word = secret_word
  letters_guessed = ""
  loss_signal = True

  print("Welcome to the game Hangman!")
  print("I am thinking of a word that is ", len(word)," letters long.")
  print("You have ", warnings_left, " left.")
  print("---------------------------------------")

  while guesses_left:
    if is_word_guessed(word, letters_guessed):
      print("Congratulations, you won!")
      print("Your total score for this game is: ", (guesses_left * (26 - len(get_available_letters(word)))))
      loss_signal = False
      break

    print("You have ", guesses_left," left.")
    print("Available letters : ",get_available_letters(letters_guessed))
    letter = input("Please guess a letter :").lower()

    if letter == '*':
      show_possible_matches(get_guessed_word(word, (letters_guessed + letter)))
      continue

    if is_word_guessed(letter, letters_guessed):
      warnings_left -= 1
      print("Oops! You've already guessed that letter. ", end="")

      if warnings_left != 0:
        print("You have ", warnings_left, " warnings left : ", get_guessed_word(word, (letters_guessed + letter)))
      else:
        guesses_left -= 1
        print("You have no warnings left, so you lose one guess. : ", get_guessed_word(word, (letters_guessed + letter)))

    elif not(letter.isalpha()):
      warnings_left -= 1
      print("Oops! That is not a valid letter. ", end="")

      if warnings_left != 0:
        print("You have ", warnings_left," warnings left: ",get_guessed_word(word, (letters_guessed + letter)))
      else:
        guesses_left -= 1
        print("You have no warnings left, so you lose one guess. : ", get_guessed_word(word, (letters_guessed + letter)))

    elif len(letter) == 1:
      if is_word_guessed(letter, word):
        print("Good guess: ", get_guessed_word(word, (letters_guessed + letter)))
      else:
        guesses_left -= 1
        print("Oops! That letter is not in my word: ", get_guessed_word(word, (letters_guessed + letter)))

    letters_guessed += letter
    print("---------------------------------------\n")

  if loss_signal:
    print("Sorry, you ran out of guesses. The word was ", word,".")
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
