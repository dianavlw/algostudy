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


if __name__ == "__main__":
    # Test case 1
    print("============== Test 1 ==============")
    players1 = 3
    deck1 = 52
    print("Player number: ", players1)
    print("Deck size:", deck1)
    test1 = CardGames(players1, deck1)
    rslt1 = test1.drawAndCompare()
    print("Winner Index: ", rslt1)
    print("Players' scores: ", test1.users_score)

    # Test case 2
    print("============== Test 2 ==============")
    players2 = 4
    deck2 = 52
    print("Player number: ", players2)
    print("Deck size: ", deck2)
    test2 = CardGames(players2, deck2)
    rslt2 = test2.drawAndCompare()
    print("Winner Index: ", rslt2)
    print("Players' scores: ", test2.users_score)

    # Test case 3
    print("============== Test 3 ==============")
    players3 = 5
    deck3 = 68
    print("Player number: ", players3)
    print("Deck size: ", deck3)
    test3 = CardGames(players3, deck3)
    rslt3 = test3.drawAndCompare()
    print("Winner Index: ", rslt3)
    print("Players' scores: ", test3.users_score)
