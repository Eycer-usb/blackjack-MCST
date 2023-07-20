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
    take = True

    while take and not current_state.is_bust() and not current_state.is_blackjack():    
        
        # Run the MCTS        
        mcts = MCTS(current_state, iteration_number)
        mcts.run()
        take = mcts.get_best_action()
        
        # Print command line options
        print("")
        print("Press 1 to take a card, 0 to stand and any other key to exit:")
        
        # Create a suggestion to the user based on the MCTS result
        suggestion = ""
        if take:
            suggestion = "(I Suggest you take a card!)"
        else:
            suggestion = "(I Suggest you stand!)"
            
        # Get user input and check for errors
        try:
            desition = int(input(suggestion + ": "))
            if desition == 0:
                print("Standing!")
                take = False
            elif desition == 1:
                print("Taking a card!")
                take = True
            else:
                print("Exiting!")
                return
        except:
            print("Invalid input!")
            print("Exiting!")
            return
        
        # Take a card if the user wants to
        if take:
            current_state = current_state.take()

        print("Current state: {}".format(current_state))

    # Check game result
    if current_state.is_bust():
        print("Bust!")
        take = False
    elif current_state.is_blackjack():
        print("Blackjack!")
        print("You Win!")
        take = False
        
    # if the user stands, the dealer plays
    else:
        print("Dealer's turn!")
        print("Dealer reveals his second card: {}".format(current_state.dealer_cards[1]))
        print("And Start Playing!")
        dealer_value = current_state.dealer_play()
        print("Dealer's value: {}".format(dealer_value))
        print("Dealer's hand: {}".format(current_state.dealer_cards))
        
        if dealer_value > 21:
            print("Dealer Bust!")
            print("You Win!")
        elif dealer_value == current_state.value:
            print("Draw!")
        elif dealer_value > current_state.value:
            print("You Lose!")
            print("House Wins!")
        
    
    print("Game Over!")
            

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