"""
Design Card Game
Constraints:

Only two players, A and B.
Only 52 unique cards, from 0 to 51.
Each card is exactly the same except for the number.
The total score of two players is always 52 / 2 = 26.
"""

import random

class CardGames:

    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.deck = list(range(52))

    def drawAndCompare(self):
        random.shuffle(self.deck)

        for i in range(0, len(self.deck), 2):
            card1 = self.deck[i]
            card2 = self.deck[i + 1]

            if card1 > card2:
                self.score1 += 1
            else:
                self.score2 += 1

        if self.score1 > self.score2:
            return "A"
        elif self.score2 > self.score1:
            return "B"
        return "TIE"

  """
  Follow-up:
Maintaining the same game rules, extend the game to include N players and M cards. 
Each player is assigned a unique index ranging from 0 to N-1, and card values range from 0 to M-1.

In each round, all N players take turns drawing cards randomly and comparing their values. T
he game continues until the remaining cards are fewer than the number of players.

Return a list of the winning players' indices. 
If multiple players achieve the highest score, they are all considered winners.
  """

import random

class CardGames:

    def __init__(self, players, deck):
        self.users_count = players
        self.users_score = [0] * self.users_count
        self.deck = list(range(deck))

    def drawAndCompare(self):
        random.shuffle(self.deck)

        index = 0

        while index + self.users_count <= len(self.deck):
            round_cards = self.deck[index:index + self.users_count]

            max_card = max(round_cards)
            winner_index = round_cards.index(max_card)

            self.users_score[winner_index] += 1

            index += self.users_count

        max_score = max(self.users_score)

        winners = []
        for i in range(self.users_count):
            if self.users_score[i] == max_score:
                winners.append(i)

        return winners
