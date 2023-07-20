"""
Class representation for a Card in the game of Blackjack
"""

class Card(int):
    def __new__(cls, value, suit, numeric_value, *args, **kwargs):
        instance = int.__new__(cls, numeric_value, *args, **kwargs)
        instance.numeric_value = numeric_value
        instance.value = value
        instance.suit = suit
        return instance

    """
    Object representation, comparison methods and mathematical operators
    """    
    def __str__(self) -> str:
        return "{}{}".format(self.value, self.suit)
    def __repr__(self) -> str:
        return "{}{}".format(self.value, self.suit)
    def __eq__(self, o: object) -> bool:
        return self.value == o.value and self.suit == o.suit

    def __hash__(self) -> int:
        return hash((self.value, self.suit))
    
    def __lt__(self, o: object) -> bool:
        return self.numeric_value < o.numeric_value
    
    def __gt__(self, o: object) -> bool:
        return self.numeric_value > o.numeric_value
    
    def __le__(self, o: object) -> bool:
        return self.numeric_value <= o.numeric_value
    def __ge__(self, o: object) -> bool:
        return self.numeric_value >= o.numeric_value
    
    def __ne__(self, o: object) -> bool:
        return self.numeric_value != o.numeric_value
    
    def __add__(self, o: object) -> int:
        return self.numeric_value + o
    
    def __sub__(self, o: object) -> int:
        return self.numeric_value - o.numeric_value
    
    def __mul__(self, o: object) -> int:
        return self.numeric_value * o.numeric_value
    
    
    
    # Getters
    def get_value(self):
        return self.value
    def get_suit(self):
        return self.suit

    # Create a maze of cards    
    def create_maze():
        suits = ['♠','♥','♦','♣']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        numeric_values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
        maze = []
        for i in range(13):
            for k in range(4):
                maze.append(Card(values[i], suits[k], numeric_values[i]))
        return maze