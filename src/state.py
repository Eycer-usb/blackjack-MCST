import random
import math
from .card import Card

"""
State class for the blackjack simulator. It is used to represent the state of the game.
"""

class State():
    # Constructor for the class
    def __init__(self, dealer_cards = [], remaining_cards = [], hand = [], parent = None, initial_state = False) -> None:
        self.simulation_number = 0
        self.simulation_value = 0
        self.hidden_card = True
        if initial_state:
            self.remaining_cards = Card.create_maze()
            self.dealer_cards = [ self.take_card(), self.take_card() ]
            self.hand = [ self.take_card(), self.take_card() ]
            self.parent = None
        else:
            self.remaining_cards = remaining_cards
            self.dealer_cards = dealer_cards
            self.hand = hand
            self.parent = parent
        
        self.value = sum(self.hand)
        self.children = []
        self.states_taken = [] 
        
    # String representation
    def __str__(self) -> str:
        if self.hidden_card:
            return "Value: {} | Hand: {} | Dealer: {}".format(self.value, self.hand, [self.dealer_cards[0], "Hidden Card"])
        return "Value: {} | Hand: {} | Dealer: {}".format(self.value, self.hand, self.dealer_cards)
    
    # String representation
    def __repr__(self) -> str:
        return "Value: {} | Hand: {} | Dealer: {}".format(self.value, self.hand, self.dealer_cards)
        
    # Hash
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
        if self.simulation_number == 0:
            return math.inf
        return self.simulation_value / self.simulation_number + math.sqrt(2 * math.log(parent.simulation_number) / self.simulation_number)
    
    # Get the best move from the children
    def get_best_move(self):
        max = -1
        best_move = self
        for child in self.children:
            if child.ucb(self) > max:
                max = child.ucb(self)
                best_move = child
        return best_move
        
    # Determine if the state is fully expanded
    def is_fully_expanded(self):
        return len(self.children) == len(self.remaining_cards)
    
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
    
    # Return a new state with a card taken
    def take(self):
        self.hand = self.hand + [self.take_card()]
        return State(self.dealer_cards, self.remaining_cards, self.hand)
    
    # Check if the state is bust
    def is_bust(self):
        return self.value > 21
    
    # Check if the state is blackjack
    def is_blackjack(self):
        return self.value == 21
    
    # Dealer start taking cards until he reaches 17
    def dealer_play(self):
        self.hidden_card = False
        dealer_value = sum(self.dealer_cards)
        while dealer_value < 17:
            self.dealer_cards.append(self.take_card())
            dealer_value = sum(self.dealer_cards)
        return dealer_value
        