# Playing Cards 3.0
# Demonstrates inheritance - overriding methods

class Card(object):
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Unprintable_Card(Card):
    """ A Card that won't reveal its rank or suit when printed"""
    def __str__(self):
        return "<unprintable>"