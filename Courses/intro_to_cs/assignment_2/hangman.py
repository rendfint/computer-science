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
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    count = 0
    for char in secret_word :
        for item in letters_guessed :
            if char == item :
                count += 1
                break
    if count == len(secret_word) :
        return True
    else :
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = ""
    for char in enumerate(secret_word) :
        if char == " " : 
            word += " "
            continue
        for item in letters_guessed :
            if char[1] == item :
                word += char[1]
                break
            else :
                continue
        if (len(word)-1) != char[0] :
            word += "_"
    return word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = []
    lowercase_letters = string.ascii_lowercase
    for letter in lowercase_letters :
        available_letters.append(letter)
        for item in letters_guessed :
            if letter == item :
                available_letters.remove(letter)
                break
    return "".join(available_letters)



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    tries = 6
    print("The hangman game, guess letters to reveal the secret word.\n" + 
        "You have " + str(tries) + " tries to guess the " + str(len(secret_word))  + 
        " letters long secret word.\n")

    lowercase_letters = string.ascii_lowercase
    letters_guessed = []

    while tries > 0 :
        available_letters = get_available_letters(letters_guessed)
        print("\nAvailable letters:", "-".join(available_letters))
        guess = input("Enter your guess (only lowercase):\n => ")

        if len(guess) == len(secret_word) :
            if guess == secret_word :
                print(" The secret word is \"" + secret_word + "\".")
                print("---You have guessed the secret word, Good Job!!---\n")
                break
            else :
                tries -= 1
                print(" That's not the secret word.")
                print(get_guessed_word(secret_word, letters_guessed))
                if tries == 1 :
                    print("\n You have", tries, "try left.")
                    continue
                elif tries == 0 :
                    print(" \nYou have no tries left, YOU LOSE.\n---The secret word was \"" + secret_word + "\".---\n")
                    break
                else :
                    print("\n You have", tries, "tries left.")
                    continue

        if len(guess) < 1 or lowercase_letters.find(guess) == -1 :
            print("\n Invalid guess. Try again.\n")
            continue

        if available_letters.find(guess) ==  -1 :
            print("\n You have guessed this letter already.Try another one.\n")
            continue

        letters_guessed.append(guess)

        print(get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed) :
            print("---You have guessed the secret word, Good Job!!---\n")
            break

        if secret_word.find(guess) >= 0 :
            print("\n-", guess, "-", "found.")
        else :
            tries -= 1
        if tries == 1 :
            print("\n You have", tries, "try left.")
            continue
        elif tries == 0 :
            print(" \nYou have no tries left, YOU LOSE.\n---The secret word was \"" + secret_word + "\".---\n")
        else :
            print("\n You have", tries, "tries left.\n")
        print("-----------------------------------------")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
