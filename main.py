import tictactoe as ttt
from os import system
import time
    
def main():

    # Init game
    system('cls')
    time.sleep(1)
    print('\nWelcome to Tictactoe.\n')
    multiplayer = input('Single player [s] or multiplayer [m]?: ')

    # Ensure user input is 's' or 'm'
    while True:
        if multiplayer.lower() == 's' or multiplayer.lower() == 'm':
            break
        time.sleep(1)
        system('cls')
        print('\nEnter "m" for multiplayer or "s" for single player.')
        multiplayer = input('Single player [s] or multiplayer [m]: ')

    # Run game
    if multiplayer.lower() == 's':
        game = ttt.Singleplayer()
        game.set_player_names()  
        game.run_game()      

    if multiplayer.lower() ==  'm':
        game = ttt.Multiplayer()
        game.set_player_names()
        game.run_game()

if __name__ == "__main__":
    main()


