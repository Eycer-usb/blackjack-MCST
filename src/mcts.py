""""
Monte Carlo Tree Search Class for the game of Blackjack
"""
from .state import State

class MCTS():
    
    """
    Constructor for the MCTS class
    args:
        root: the root node of the tree
        iteration_number: the number of iterations to run the simulation
        
    methods:
        run: run the simulation
        get_best_move: get the best move from the root node
        select: select a node to expand
        expand: expand the selected node
        backpropagate: backpropagate the simulation result
    """
    def __init__(self, root, iteration_number):
        self.root = root
        self.iteration_number = iteration_number
    
    # Run the simulation
    def run(self):
        for i in range(self.iteration_number):
            node = self.select()
            node = self.expand(node)
            value = self.simulate(node)
            self.backpropagate(node, value)
    
    # Select a node to expand
    def select(self):
        selected = self.root
        while selected.is_fully_expanded():
            selected = selected.get_best_move()
        return selected
    
    # Expand the selected node
    def expand(self, node):
        return node.create_child()
    
    # Simulate the game
    def simulate(self, node):
        return node.simulate()
    
    # Backpropagate the simulation result
    def backpropagate(self, node, value):
        while node != None:
            node.simulation_number += 1
            node.simulation_value += value
            node = node.parent
    