"""
Design Card Game
Create a simulation of a card game. The game involves a deck of unique cards represented by integers. 
Assume there are only 2 players "A" and "B", and a deck of 52 unique cards (numbered from 0 to 51). 
Players "A" and "B" take turns drawing cards randomly from the deck. After each draw, the players compare their cards:

If Player A's card is higher, Player A earns 1 point.
If Player B's card is higher, Player B earns 1 point.
The game continues until all cards have been drawn and compared. The player with the higher score wins the game. 
If scores are tied at the end, return "TIE". Note that your solution should simulate the entire drawing process.

Implement the CardGames class:

CardGames(): Initializes the card game.
String drawAndCompare(): Players take turns drawing and comparing card values until all cards are drawn. 
Returns the winner or "TIE" if the scores are equal.
Constraints:

Only two players, A and B.
Only 52 unique cards, from 0 to 51.
Each card is exactly the same except for the number.
The total score of two players is always 52 / 2 = 26.
Example

Input:
["CardGames", "drawAndCompare"]
[[], []]

Output:
[null, "A"]
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
            card2 = self.deck[i+1]

            if card1 > card2:
                self.score1 +=1
            else:
                self.score2 += 1
        if self.score1 > self.score2:
            return "A"
        elif self.score2 > self.score1:
            return "B"
        return "TIE"



if __name__ == "__main__":
    def test(i):
        game = CardGames()
        res = game.drawAndCompare()
        print("======== Test {0} =======".format(i))
        print("Player A's score: {0}, palyer B's score: {1}".format(game.score1, game.score2))
        print("The result is: " + res)

    for i in range(1,6):
        test(i)
