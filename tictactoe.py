from os import system
import time
import random

class Multiplayer:
    def __init__(self):
        self.player_one = 'Player One'
        self.player_two = 'Player Two'
        self.grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.game_running = False
        self.player_turn = random.randint(1,2)
        self.select_column = int()
        self.select_row = int()

    def print_grid(self):
        self.clear()
        print('\n')
        for row in self.grid:
            print(row)
        print('\n')
        
    def clear(self):
        time.sleep(1)
        system('cls')

    def set_player_names(self):
        self.clear()
        self.player_one = input('\nPlayer one, enter your name: ')
        self.clear()
        self.player_two = input('\nPlayer two, enter your name: ') 

    def check_grid_entry(self):
        if self.select_column not in range(1, 4) or self.select_row not in range(1, 4):
            print('\nInvalid input. Please use column/row 1, 2 or 3.')
            time.sleep(2)
            self.run_game()            
        if not self.grid[self.select_row-1][self.select_column-1] == 0:
            print('\nError. You cannot go there.')
            time.sleep(2)
            self.run_game()
    
    def check_win(self):
        None

    def run_game(self):
        self.game_running = True
        while self.game_running:
            self.print_grid()
            if self.player_turn == 1:
                print('{}, it is your turn.'.format(self.player_one))
                self.select_column = int(input('\nSelect column: '))
                self.select_row = int(input('Select row: '))
                self.check_grid_entry()
                self.grid[self.select_row-1][self.select_column-1] = 1
                self.check_win()
                self.player_turn = 2
            elif self.player_turn == 2:
                print('\n{}, it is your turn.'.format(self.player_two))
                self.select_column = int(input('\nSelect column: '))
                self.select_row = int(input('Select row: '))
                self.check_grid_entry()
                self.grid[self.select_row-1][self.select_column-1] = 2
                self.check_win()
                self.player_turn = 1

        

class Singleplayer:

    def __init__(self, player_one):
        self.player_one = player_one

        