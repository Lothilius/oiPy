# Files: Solver.py
#
# Description: Solves a jumble by implementing a word list tree of unsorted type from a
# file of single column list of words.
#
__author__ = 'lothilius'

import sys
import time
from Wordlist import *
from Permutations import *


def main():
    while True:
        try:
            inputFileName = input("Enter full path of scrambled word list:")
            f = open(inputFileName)
            break
        except FileNotFoundError:
            print("\nThe directory is invalid. Please try again.")

    start = time.time()
    print("\nUsing binary tree wordList.")
    wordList = BinaryTreeWordList()
    print("Creating wordList.", end="\n")

    # We only add words to the Wordlist if they have 5 or 6 letters.
    wordList.addWordsFromFile(inputFileName, lambda x: len(x) in [4, 13])
    print("The Wordlist contains ", len(wordList), " words.")
    end = time.time()
    print("Building the Wordlist took %2.3f seconds" % (end - start))
    
    # Execute this loop until the user decides to exit.
    start = time.time()

    while True:
        word = input("\nEnter a scrambled word (or EXIT):  ")
        word = word.strip().lower()
        # See if the word contains bad characters.
        if not word.isalpha():
            print("Word contains illegal characters. Try again")
            continue
        # Should we terminate
        elif word == 'exit':
            print("\nThanks for playing!  Goodbye.", end="\n\n")
            break
        # There's no need searching the Wordlist if the word isn't
        # a plausible length.
        elif not len(word) in range(4, 13):
            print( "Word must have 4 to 13 letters.  Try again")
            continue
        else:
            break

    # Create a list of all permutations of the input
    # string.

    # print out how many unique perms there are.
    permsCount, uniquePermsCount = Permutations.howManyPerms(word)
    print("Found ", permsCount, "permutations; ", uniquePermsCount, "unique permutations")

    # We're going to check how many permutations we generated, and
    # how many comparisons were made against words in the wordList.
    permutationsChecked = 0
    comparisonsMade = 0

    # Iterate through the permutations until you find one that is
    # in the wordList, or fail if there are no hits.
    found = False
    for p in Permutations.allPerms(word):
        permutationsChecked += 1
        permInList, comparisons = wordList.findWord(p)
        comparisonsMade += comparisons
        if permInList:
            print("Found word: " + p)
            found = True
            # With the break, stops after the first hit.  Without it,
            # this tries all of the permutations.
            break
    if not found:
        print("Sorry. I can't solve this jumble!  Try again.")
    end = time.time()

    # Print out the stats on this attempt.
    print("Solving this jumble took %2.5f seconds" % (end - start))
    print("Checked ", permutationsChecked, " permutations.")
    print("Made ", comparisonsMade, " comparisons.")



main()

