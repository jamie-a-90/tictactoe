from os import system
import time
import random

class Multiplayer:
    def __init__(self):
        self.player_one = 'Player One'
        self.player_two = 'Player Two'
        self.player_turn = 2# random.randint(1,2)
        self.__grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.__alive = True
        self.__select_column = str()
        self.__select_row = str()
        self.__input_valid = True 

    # Print __grid in console
    def __print___grid(self, message=None):
        self.__clear()
        if message:
            print(message)
        print('\n')
        for row in self.__grid:
            print('     ' + str(row))
        print('\n')
        
    # Clear console
    def __clear(self):
        time.sleep(1)
        system('cls')

    # Check for invalid input
    def __check___grid_entry(self):
        if not self.__select_column.isnumeric() or not self.__select_row.isnumeric(): # Check to ensure input is numeric
            print('\nInvalid input. Please use column/row 1, 2 or 3.')
            time.sleep(2)
        if int(self.__select_column) not in range(1, 4) or int(self.__select_row) not in range(1, 4): # Check input is a valid number. 1, 2 or 3
            print('\nInvalid input. Please use column/row 1, 2 or 3.')
            time.sleep(2) 
        if not self.__grid[int(self.__select_row)-1][int(self.__select_column)-1] == 0: # Check to ensure __grid space hasn't already been taken
            print('\nYou cannot go there. Already taken.')
            time.sleep(2)
        else:
            self.__input_valid = False
        
    # Check win condition. Across, down, diagonal and draw 
    def __check_win(self):
        def check_rows():
            for row in self.__grid:
                if set(row) == {1}:
                    self.__alive = False
                    self.__print___grid(message='\n##### Player 1 #####')
                    print("Player one wins!\n")
                if set(row) == {2}:
                    self.__alive = False
                    self.__print___grid(message='\n##### Player 2 #####')
                    print("Player two wins!\n")  

        def check_columns():
            if (set([self.__grid[0][0], self.__grid[1][0], self.__grid[2][0]]) == {1} or
                    set([self.__grid[0][1], self.__grid[1][1], self.__grid[2][1]]) == {1} or 
                    set([self.__grid[0][2], self.__grid[1][2], self.__grid[2][2]]) == {1}):
                self.__alive = False
                self.__print___grid(message='\n##### Player 1 #####')
                print("Player one wins!\n")
            if (set([self.__grid[0][0], self.__grid[1][0], self.__grid[2][0]]) == {2} or
                    set([self.__grid[0][1], self.__grid[1][1], self.__grid[2][1]]) == {2} or 
                    set([self.__grid[0][2], self.__grid[1][2], self.__grid[2][2]]) == {2}):
                self.__alive = False
                self.__print___grid(message='\n##### Player 2 #####')
                print("Player two wins!\n")

        def check_diagonal():
            if (set([self.__grid[0][0], self.__grid[1][1], self.__grid[2][2]]) == {1} or
                    set([self.__grid[0][2], self.__grid[1][1], self.__grid[2][0]]) == {1}):
                self.__alive = False
                self.__print___grid(message='\n##### Player 1 #####')
                print("Player one wins!\n")
            if (set([self.__grid[0][0], self.__grid[1][1], self.__grid[2][2]]) == {2} or
                    set([self.__grid[0][2], self.__grid[1][1], self.__grid[2][0]]) == {2}):
                self.__alive = False
                self.__print___grid(message='\n##### Player 2 #####')
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
        while self.__alive:
            if self.player_turn == 1:
                while self.__input_valid:
                    self.__print___grid(message='\n##### Player 1 #####')
                    print('{}, it is your turn.'.format(self.player_one))
                    self.__select_column = input('\nSelect column: ')
                    self.__select_row = input('Select row: ')
                    self.__check___grid_entry()
                self.__grid[int(self.__select_row)-1][int(self.__select_column)-1] = 1
                self.__check_win()
                if not self.__alive:
                    break
                else:
                    self.player_turn = 2
                    self.__input_valid = True
            if self.player_turn == 2:
                while self.__input_valid:
                    self.__print___grid(message='\n##### Player 2 #####')
                    print('{}, it is your turn.'.format(self.player_two))
                    self.__select_column = input('\nSelect column: ')
                    self.__select_row = input('Select row: ')
                    self.__check___grid_entry()
                self.__grid[int(self.__select_row)-1][int(self.__select_column)-1] = 2
                self.__check_win()
                if not self.__alive:
                    break
                else:
                    self.player_turn = 1
                    self.__input_valid = True


class Singleplayer:

    def __init__(self, player_one):
        self.player_one = player_one

        