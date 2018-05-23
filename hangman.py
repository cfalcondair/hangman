"""Script to play hangman with."""
import sys
import re

from random_word import random_word
import inflect

class Hanger(object):
    """The hanger that is checking the letters you've guessed against what is required.

    Attributes:
        word: A string holding the desired word
        guessed_word: An array of each of the letters that represents the guesses
            of the word
        guesses: How many guesses until hangman gets hung.
    """

    def __init__(self, word, guesses = 3):
        """Return a Hanger object with looking for the word *word*"""
        print("Let's play hangman!\n")
        self.word = word
        self.guessed_word = len(word) * ["_"]
        self.guesses = guesses

    def indices(self, char):
        """Returns the indices of the letter *letter* in the word"""
        return [i for i, ltr in enumerate(self.word) if ltr == char]

    def insert_guess(self, char, indices):
        """Inserts the guessed char into the guessed word"""
        for index in indices:
            self.guessed_word[index] = char

    def valid_guess(self, char):
        """Checks whether the char guess a single valid letter"""
        reg = re.compile('[A-Za-z]+')
        if type(char) != str:
            print("guess must be a string")
            return False
        elif len(char) != 1:
            print("length of the guess must be 1")
            return False
        elif not reg.match(char):
            print("guess must be a letter")
            return False
        return True

    def guess(self, char):
        """inserts the character into the guessed word and
            prints the status of the guesses and the word"""
        lower_char = char.lower()
        is_valid = self.valid_guess(lower_char)
        if not is_valid:
            return

        if char in self.guessed_word:
            print("Already guessed that letter... ")
            return
        indices = self.indices(lower_char)
        if len(indices) > 0:
            print("Great! Correctly guessed a letter")
        else:
            self.guesses -= 1
            print("Whoops! That letter does NOT exist in this word. Sooooori.")
        self.insert_guess(lower_char, indices)
        if self.word_guessed():
            print("Correct! You worked out the word is...\n\n{word}!!".format(word=self.word.upper()))
        elif self.guesses > 0:
            print("Only {guess_count} {guesses} left".format(guess_count=self.guesses, guesses=inflect.engine().plural("guess",self.guesses)))
        else:
            print("\nOh no. Well the hangman is hung now. The word was:\n\n{word}\n\nHow'd you not get that...".format(word=self.word))

    def word_guessed(self):
        """Checks if the word has been all guessed"""
        return self.guessed_word.count("_") == 0

    def any_guesses_left(self):
        """Returns a boolean response whether there are any guesses left"""
        return self.guesses > 0

    def game_over(self):
        """Returns a boolean response whether the game is over or not"""
        return not self.any_guesses_left() or self.word_guessed()

    def print_status(self):
        print("The word is {current_word}".format(current_word=self.guessed_word))

def main():
    """Entry point for the game"""

    hanger = Hanger(random_word())
    while True:
        hanger.print_status()
        char = input("\nHave guess at a letter:\n")
        print("")
        hanger.guess(char)
        if hanger.game_over():
            break

if __name__ == '__main__':
    sys.exit(main())
