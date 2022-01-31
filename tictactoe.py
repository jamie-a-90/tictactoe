from os import system
import time
import random

class Multiplayer:
    def __init__(self):
        self.player_one = 'Player One'
        self.player_two = 'Player Two'
        self.grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.game_running = False
        self.player_turn = 2# random.randint(1,2)
        self.select_column = str()
        self.select_row = str()

    # Print grid in console
    def __print_grid(self, message=None):
        self.__clear()
        if message:
            print(message)
        print('\n')
        for row in self.grid:
            print('     ' + str(row))
        print('\n')
        
    # Clear console
    def __clear(self):
        time.sleep(1)
        system('cls')

    # Check for invalid input
    def __check_grid_entry(self):
        if not self.select_column.isnumeric() or not self.select_row.isnumeric(): # Check to ensure input is numeric
            print('\nInvalid input. Please use column/row 1, 2 or 3.')
            time.sleep(2)
            self.run_game()
        if int(self.select_column) not in range(1, 4) or int(self.select_row) not in range(1, 4): # Check input is a valid number. 1, 2 or 3
            print('\nInvalid input. Please use column/row 1, 2 or 3.')
            time.sleep(2)
            self.run_game()           
        if not self.grid[int(self.select_row)-1][int(self.select_column)-1] == 0: # Check to ensure grid space hasn't already been taken
            print('\nYou cannot go there. Already taken.')
            time.sleep(2)
            self.run_game()
    
    # Check win condition. Across, down, diagonal and draw 
    def __check_win(self):
        def check_rows():
            for row in self.grid:
                if set(row) == {1}:
                    self.game_running = False
                    self.__print_grid(message='\n##### Player 1 #####')
                    print("Player one wins!\n")
                if set(row) == {2}:
                    self.game_running = False
                    self.__print_grid(message='\n##### Player 2 #####')
                    print("Player two wins!\n")  

        def check_columns():
            if (set([self.grid[0][0], self.grid[1][0], self.grid[2][0]]) == {1} or
                    set([self.grid[0][1], self.grid[1][1], self.grid[2][1]]) == {1} or 
                    set([self.grid[0][2], self.grid[1][2], self.grid[2][2]]) == {1}):
                self.game_running = False
                self.__print_grid(message='\n##### Player 1 #####')
                print("Player one wins!\n")
            if (set([self.grid[0][0], self.grid[1][0], self.grid[2][0]]) == {2} or
                    set([self.grid[0][1], self.grid[1][1], self.grid[2][1]]) == {2} or 
                    set([self.grid[0][2], self.grid[1][2], self.grid[2][2]]) == {2}):
                self.game_running = False
                self.__print_grid(message='\n##### Player 2 #####')
                print("Player two wins!\n")

        def check_diagonal():
            check_diag_one = [self.grid[0][0], self.grid[1][1], self.grid[2][2]]
            check_diag_two = [self.grid[0][2], self.grid[1][1], self.grid[2][0]]
            if set(check_diag_one) == {1} or set(check_diag_two) == {1}:
                self.game_running = False
                self.__print_grid(message='\n##### Player 1 #####')
                print("Player one wins!\n")                
            if set(check_diag_one) == {2} or set(check_diag_two) == {2}:
                self.game_running = False
                self.__print_grid(message='\n##### Player 2 #####')
                print("Player two wins!\n")  
            
        def check_draw():
            None

        check_rows()
        check_columns()
        check_diagonal()
        check_draw()
    
    # Set player names for player 1 and player 2
    def set_player_names(self):
        self.__clear()
        self.player_one = input('\nPlayer one, enter your name: ')
        self.__clear()
        self.player_two = input('\nPlayer two, enter your name: ') 

    # Run main game logic
    def run_game(self):
        self.game_running = True
        while self.game_running:
            if self.player_turn == 1:
                self.__print_grid(message='\n##### Player 1 #####')
                print('{}, it is your turn.'.format(self.player_one))
                self.select_column = input('\nSelect column: ')
                self.select_row = input('Select row: ')
                self.__check_grid_entry()
                self.grid[int(self.select_row)-1][int(self.select_column)-1] = 1
                self.__check_win()
                self.player_turn = 2
            elif self.player_turn == 2:
                self.__print_grid(message='\n##### Player 2 #####')
                print('{}, it is your turn.'.format(self.player_two))
                self.select_column = input('\nSelect column: ')
                self.select_row = input('Select row: ')
                self.__check_grid_entry()
                self.grid[int(self.select_row)-1][int(self.select_column)-1] = 2
                self.__check_win()
                self.player_turn = 1

        

class Singleplayer:

    def __init__(self, player_one):
        self.player_one = player_one

        