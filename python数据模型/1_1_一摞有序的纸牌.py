# -*- coding:utf-8 -*-

"""
# Author ：li zi hao
"""

import collections
import random
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades hearts diamonds clubs '.split()

    def __init__(self):
        self.cards = [Card(rank, suit)
                      for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, item):
        return self.cards[item]


if __name__ == '__main__':
    deck = FrenchDeck()
    for i in deck:
        print(i)
    # suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    #
    # def spades_high(card):
    #     suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    #     rank_value = FrenchDeck.ranks.index(card.rank)
    #     return rank_value * len(suit_values) + suit_values[card.suit]
    #
    # for card in sorted(deck, key=spades_high):
    #     print(card)
