import random
import math
from card import Card

"""
State class for the blackjack simulator. It is used to represent the state of the game.
"""

class State():
    # Constructor for the initial state
    def __init__(self) -> None:
        self.simulation_number = 0
        self.simulation_value = 0
        self.remaining_cards = Card.create_maze()
        self.dealer_cards = [ self.take_card(), self.take_card() ]
        self.hand = [ self.take_card(), self.take_card() ]
        self.value = sum(self.hand)
        self.parent = None
        self.children = []
        self.states_taken = [] 
        
    # Constructor for a state with a given dealer hand, remaining cards and player hand
    def __init__(self, dealer_cards, remaining_cards, hand, parent = None) -> None:
        self.value = 0
        self.simulation_number = 0
        self.simulation_value = 0
        self.dealer_cards = dealer_cards
        self.remaining_cards = remaining_cards
        self.hand = hand
        self.parent = parent
        self.children = []
        self.states_taken = [] 
    
        
    # String representation
    def __str__(self) -> str:
        return "Value: {} | Dealer: {} | Hand: {} | Remaining: {}".format(self.value, self.dealer_cards, self.hand, self.remaining_cards)
    
    # String representation
    def __repr__(self) -> str:
        return "Value: {} | Dealer: {} | Hand: {} | Remaining: {}".format(self.value, self.dealer_cards, self.hand, self.remaining_cards)
    
    # Equality
    def __eq__(self, o: object) -> bool:
        return self.dealer_cards == o.dealer_cards and self.remaining_cards == o.remaining_cards and self.hand == o.hand
    def __hash__(self) -> int:
        return hash((tuple(self.dealer_cards), tuple(self.remaining_cards), tuple(self.hand)))
    
    # Take a card from the deck. If remove is true, remove the card from the deck
    def take_card(self, remove=True):
        card = random.choice(self.remaining_cards)
        if remove:
            self.remaining_cards.remove(card)
        return card
    
    # Check if the state is terminal
    def not_terminal(self):
        return self.value < 21
    
    # Calculate the UCB value
    def ucb(self, parent):
        return self.simulation_value / self.simulation_number + math.sqrt(2 * math.log(parent.simulation_number) / self.simulation_number)
    
    # Get the best move from the children
    def get_best_move(self):
        return max(self.children, key=lambda x: x.ucb(self))
    
    # Determine if the state is fully expanded
    def is_fully_expanded(self):
        return len(self.children) == len(self.actions_taken)
    
    # Create a child state, add it to the children list and to the actions taken list
    # Return the child state
    def create_child(self):
        if not self.not_terminal():
            return self
        
        card = self.take_card(False)
        while card in self.states_taken:
            card = self.take_card(False)
        new_state = State(self.dealer_cards, [x for x in self.remaining_cards if x != card]  ,
                          self.hand + [card], self)
        self.children.append(new_state)
        self.states_taken.append(card)
        return new_state
                
    # Makes a simulation of the game starting from the current state
    def simulate(self):
        if not self.not_terminal():
            return self.value
        new_state = State(self.dealer_cards, self.remaining_cards, self.hand)
        while new_state.not_terminal():
            card = new_state.take_card(False)
            new_state = State(self.dealer_cards, [x for x in new_state.remaining_cards if x != card]  ,
                              new_state.hand + [card])
        return new_state.value
        
        