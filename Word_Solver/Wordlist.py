# Files: Wordlist.py
# Description: Creates word list. Either flat and unsorted with a linear search, or a sorted list implementing a binary search.  
__author__ = 'lothilius'

import time
from Trees import *

class Wordlist:
    """A Wordlist stores an arbitrary number of words.  The main
        function is to be able to ask whether or not a word is
        in the Wordlist.  We can also add and remove words.
    """

    def __init__(self):
        """Create an empty Wordlist."""
        self._words = []
        self._wordCount = 0

    def __len__(self):
        return self._wordCount

    def isEmpty(self):
        return not self._words

    def addWord(self, word, f):
        """Add a single word to the Wordlist."""
        if f(word):
            self._words.append(word)
            self._wordCount += 1

    def addWordsFromFile( self, filename, f):
        """Given an external file containing words, add
            each to the Wordlist.  Assume that the file
            contains one word per line, and that the words
            do not repeat.
        """
        inputFile = open(filename, 'r')
        count = 0
        for line in inputFile:
            time1 = time.time()
            word = line.strip()
            self.addWord(word, f)
        inputFile.close()

    def removeWord(self, word):
        """This removes the first occurrence of the word.
            Assumes only one occurrence."""
        if self.findWord(word):
            self._words.remove(word)
            self._wordCount -+ 1
        else:
            print("Word", word, "not found in wordlist.")

    def findWord(self, word):
        """Find a word in the Wordlist via linear search.  This
            could use the Python in operator, but that would be
            difficult to meter.  Returns a pair containing the
            boolean result and the number of comparisons made.
        """
        for i in range(len(self._words)):
            if self._words[i] == word:
                return (True, i+1)
        return (False, len(self._words))


# class SortedWordList(Wordlist):
#     """An implementation of Wordlist that has the words sorted."""
#     def __init__(self):
#         """Create an empty Wordlist."""
#         self._words = []
#         self._wordCount = 0
#
#     def addWord(self, word, f):
#         """Add a single word to the Wordlist."""
#         splitWord = list(word)
#         #Append to list if empty
#         if SortedWordList.isEmpty(self):
#             self._words.append(word)
#             self._wordCount += 1
#         elif f( word ):
#             for index in range(len(self._words)):
#                 if self._words[index] > word:
#                     self._words.insert(index, word)
#                     self._wordCount += 1
#                     break
#                 elif index == len(self._words)-1:
#                     self._words.append(word)
#                     self._wordCount += 1
#
#     def binarySearch(Wordlist, x, lo, hi):
#         """This implements a binary search for x on a
#             list lst, between indices lo and hi.  The index
#             is returned if x is found, else -1 is returned.
#         """
#         comparisons = 0
#         while lo < hi:
#             comparisons += 1
#             mid = (lo + hi)//2
#             midval = Wordlist[mid]
#             if midval < x:
#                 lo = mid+1
#             elif midval > x:
#                 hi = mid
#             else:
#                 return (mid, comparisons)
#         return -1, comparisons
#
#     def findWord(self, word):
#         """Find a word in the Wordlist via binary search.  This
#             could use the Python in operator, but that would be
#             difficult to meter.  Returns a pair containing the
#             boolean result and the number of comparisons made.
#         """
#         comp = SortedWordList.binarySearch(self._words, word, 0, len(self._words))
#         if comp[0] == -1:
#             return (False, len( self._words))
#         else:
#             return (True, comp[0])


class BinaryTreeWordList(Wordlist):
    """A BinaryTreeWordList stores an arbitrary number of words in a binary tree structure.
        The main function is to be able to ask whether or not a word is
        in the Wordlist.  We can also add and remove words.
    """
    
    def __init__(self):
        Wordlist.__init__(self)
        self._wordtree = BinarySearchTree()
    
    def __len__(self):
        return self._wordCount
    
    def isEmpty(self):
        return not self._wordtree
    
    def addWord(self, word, f):
        """Add a single word to the Wordlist."""
        if f(word):
            BinarySearchTree.insert(self._wordtree, word)
            self._wordCount += 1
    
    def findWord(self, word):
        """Find a word in the Wordlist via search of a binary tree.
            Returns a pair containing the
            boolean result and the number of comparisons made.
        """
        
        if self._wordtree.inTree(word):
            return True, BinaryTreeNode.nodeDepth(self._wordtree.getRoot(), word)
        else:
            return False, BinaryTreeNode.nodeDepth(self._wordtree.getRoot(), word)
