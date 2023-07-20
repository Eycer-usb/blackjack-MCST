import random
from src.state import State
import sys
from src.mcts import MCTS

"""
    Client script for the blackjack simulator.
    
    Usage: python blackjack_simulator.py [iteration_number]
    args:   iteration_number: number of iterations to run the simulation
    output: prints the current state of the game after each iteration        
"""

def main(args=sys.argv[1:]):
    
    # Check for help
    if( len(args) > 0 and args[0] == "help" ):
        help()
        return
    
    if len(args) > 1:
        print("Too many arguments!")
        help()
        return
    
    # Print welcome message
    print("Welcome to the Blackjack Simulator!")
    iteration_number = 100
    
    # Check for iteration number
    if( len(args) > 0 ):
        try:
            iteration_number = int(args[0])
        except:
            print("Invalid argument!")
            help()
            return
        
    # Print iteration number  
    print("Running {} iterations...".format(iteration_number))
    
    # Create a new game
    root = State(initial_state=True)
    print("Initial state: {}".format(root))
        
    # Run the Game
    current_state = root
    while current_state.not_terminal():
        mcts = MCTS(current_state, iteration_number)
        mcts.run()
        current_state = current_state.get_best_move()
        print("Current state: {}".format(current_state))

"""
    Helper function for printing help message
    args:   None
    output: prints the help message
"""
def help():
    print("Usage: python blackjack_simulator.py [iteration_number]")
    print("args:   iteration_number: number of iterations to run the simulation")
    print("output: prints the current state of the game after each iteration")

if __name__ == "__main__":
    main()