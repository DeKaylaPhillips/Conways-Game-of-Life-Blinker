# Run the file to start the interface! --> python GameOfLifeSolo.py or python3 GameOfLifeSolo.py

import time

class Game_Of_Life:
    def __init__(self, rows=3, columns=3):
        self.rows = rows
        self.columns = columns
        self.gridArr = []
        self.gridStr = ''

    def start_interface(self):
        answer = input("Welcome to Conway's Game of Life. Would you like to see the 3x3 blinker pattern? Select Y or N.\n\n")
        
        if answer.casefold() == 'y':
            print('\nHere is your grid!\n')
            return self.create_grid()  
        elif answer.casefold() == 'n':
            print('\nExiting the game. Goodbye!\n')
            return quit()
        print('\nInvalid input! Try again.\n')
        return self.start_interface()


    def create_grid(self): 
        print('Here is the grid that will contain your 3x3 blinker pattern: \n')

        for row in range(self.rows):
            row = [0] * self.columns
            self.gridArr.append(row)
        
        for rows in self.gridArr:
            print(rows)
        
        return self.selection()

    def selection(self):
        answer = input('\nWould you like to start? Select Y or N.\n\n')
        
        if answer.casefold() == 'y':
            print("\n--- 1's represent active cells. ---\n")
            return self.start_game()
        
        elif answer.casefold() == 'n': 
            print('Exiting the game. Goodbye!')
            return quit()
        
        print('Invalid input! Try again.')
        return self.create_grid()
        
    def start_game(self):
        pattern = 0

        for _ in range(10):
            if pattern == 0:
                self.horizontal_cells()
                pattern = 1
                time.sleep(.7)

            elif pattern == 1:
                self.vertical_cells()
                pattern = 0
                time.sleep(.7)

            print('\n')
        
        return 'This is the oscillating blinking pattern. :)'

    def horizontal_cells(self):
        self.gridArr[1] = [1] * self.columns    
        
        for rows in self.gridArr:               
            print(rows)
        
        self.gridArr[1] = [0] * self.columns
        
        return self.gridArr
            
    def vertical_cells(self):
        for rows in self.gridArr:       
            rows[1] = 1
            print(rows)

        for rows in self.gridArr:
            rows[1] = 0

        return self.gridArr

game = Game_Of_Life()
print(game.start_interface()) # Don't touch this line! Code not yet optimized to function with more complex patterns/grids :( !

# TO-DO: ADD TEST SUITE.


