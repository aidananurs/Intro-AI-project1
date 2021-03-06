import pygame
from .constants import ROWS, COLS, BLUE, WHITE, GREEN, RED, RADIUS
from .drawing_transition_matrix import x_cord, y_cord
from .pegs import Peg
from .start_board import start_board


class BoardClass:
    def __init__(self):
        self.board = []
        self.red_ingoal = self.green_ingoal = 0
        self.create_board()
    #Drawing the board (only white circles/spaces)
    def draw_circles(self, win):
        win.fill(BLUE)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.circle(win, WHITE, [x_cord[row, col], y_cord[row, col]], RADIUS, 0)
    #changing the position in the 'board' list for the peg that we want to move
    #and space that we want to move it to
    def move(self, peg, row, col):
        self.board[peg.row][peg.col], self.board[row][col] = self.board[row][col], self.board[peg.row][peg.col]
        peg.move(row, col)

    def get_peg(self, row, col):
        return self.board[row][col]
    #Adding pegs to the board/creating board list
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if start_board[row, col] == 1:
                    self.board[row].append(Peg(row, col, RED))
                elif start_board[row, col] == 2:
                    self.board[row].append(Peg(row, col, GREEN))
                else:
                    self.board[row].append(0)
    #Drawing pegs
    def draw(self, win, selected):
        self.draw_circles(win)
        for row in range(ROWS):
            for col in range(COLS):
                Peg = self.board[row][col]
                if Peg != 0:
                    Peg.draw(win, selected)
    #checking how many pegs are in the goal state for both players               
    def goalstate(self):
        self.red_ingoal = self.green_ingoal = 0
        for i in range(ROWS):
            for j in range(COLS):
                peg=self.board[i][j]
                if peg !=0:
                    if peg.color == RED and start_board[i,j] == 2:
                        self.red_ingoal += 1
                    if peg.color ==  GREEN and start_board[i,j] == 1:
                        self.green_ingoal += 1 
    #checking the winning conditions    
    def winner(self):
        if self.red_ingoal == 6:
            return RED
        elif self.green_ingoal == 6:
            return GREEN
        
        return None
    #Getting the list of all possible move for a specific peg
    def get_valid_moves(self, Peg):
        moves = []
        row = Peg.row
        col = Peg.col

        #all hopOne moves
        moves = self.hopOne(row, col)
        #all hopOver moves
        moves = self.hopOver(row, col, moves)


        return moves
    #Checking if specific peg can move one space away
    def hopOne(self, row, col):
        moves = []
        # down
        if row + 1 <= 5 and self.board[row + 1][col] == 0:
            moves.append([row + 1, col])
        # up
        if row - 1 >= 0 and self.board[row - 1][col] == 0:
            moves.append([row - 1, col])
        # right
        if col + 1 <= 5 and self.board[row][col + 1] == 0:
            moves.append([row, col + 1])
        # left
        if col - 1 >= 0 and self.board[row][col - 1] == 0:
            moves.append([row, col - 1])

        return moves
    #Checking if specific peg can move jump over other pegs
    #This function is recurring so its allows to make multiply jumps
    def hopOver(self, row, col, moves):

        if row + 2 <= 5 and self.board[row + 1][col] != 0 and self.board[row + 2][col] == 0 and [row + 2, col] not in moves:
            moves.append([row + 2, col])

            moves = self.hopOver(row + 2, col, moves)

        if row - 2 >= 0 and self.board[row - 1][col] != 0 and self.board[row - 2][col] == 0 and [row - 2, col] not in moves:
            moves.append([row - 2, col])

            moves = self.hopOver(row - 2, col, moves)

        if col + 2 <= 5 and self.board[row][col + 1] != 0 and self.board[row][col + 2] == 0 and [row, col + 2] not in moves:
            moves.append([row, col + 2])

            moves = self.hopOver(row, col + 2, moves)

        if col - 2 >= 0 and self.board[row][col - 1] != 0 and self.board[row][col - 2] == 0 and [row, col - 2] not in moves:
            moves.append([row, col - 2])

            moves = self.hopOver(row, col-2, moves)
        return moves
    #returning list of all pegs on the board   
    def get_all_pegs(self, colour):
        pegs = []
        for row in self.board:
           for peg in row:
               if peg != 0 and peg.color == colour:
                   pegs.append(peg)
        return pegs
    
    def get_board(self):
        return self.board
    #Calculating the evaluation function   
    def evaluate(self):
        h=0
        for i in range(ROWS):
            for j in range(COLS):
                peg=self.board[i][j]
                if peg != 0:
                    if peg.color == RED:
                        h+=j+(5-i)
                    if peg.color == GREEN:
                        h-=(5-j)+i
        self.goalstate()
        h+=10*self.red_ingoal
        h-=10*self.green_ingoal 
        return h    