import numpy as np

class Cell:
    def __init__(self):
        self.state = False
    
    def __repr__(self):
        if self.state :
            return "'c = Cell()' \n'c.turn_on()'"
        else:
            return "'Cell()'"
    
    def __str__(self):
        if self.state:
            return "Active Cell object"
        else:
            return "Inactive Cell object"

    def turn_on(self):
        self.state = True



class Board:
    def __init__(self, n=5):
        self.size = n
        self.board = [[Cell() for _ in range (self.size)] for __ in range(self.size)]
        self.gen = 0
    
    def __repr__(self):
        return "'Board({})'".format(self.size)
    
    def __str__(self):
        shape = '{0}x{0}'.format(self.size)
        if self.gen == 1:
            gen = '1st gen. '
        elif self.gen == 2:
            gen = '2nd gen. '
        elif self.gen == 3:
            gen = '3rd gen. '
        else:
            gen = '{}th gen. '.format(self.gen)
        
        return gen + shape + 'Board object' + self.str_board()

    def random_population(self, on_fraction = 0.15):
        i, j = 0, 0
        for row in self.board:
            for c in row:
                p = np.random.rand()
                if p < on_fraction:
                    c.turn_on()
                j += 1
            i += 1
            j = 0
    

    def str_board(self):
        str_board = ''
        for row in self.board:
            str_board = str_board + '\n'
            for c in row:
                if c.state:
                    str_board = str_board + '-- '
                else:
                    str_board = str_board + '## '
            
        return str_board

    def neighbour_matrix(self):
        self.n_matrix = [[0 for _ in range(self.size)] for __ in range(self.size)]

        for y in range(self.size):
            for x in range(self.size):
                left = max(0, x-1)
                right = min(self.size, x + 2)
                down = max(0, y-1)
                up = min(self.size, y + 2)
                
                neigh = 0
                for yneigh in range(down, up):
                    for xneigh in range(left, right):
                        if ((xneigh == x) and (yneigh == y)):
                            pass
                        
                        elif self.board[xneigh][yneigh].state:
                            neigh += 1                        
                        else:
                            pass

                self.n_matrix[x][y] = neigh
              
        return self.n_matrix
    
    def next_gen(self, rule='B3/S23'):
        next_board = [[Cell() for _ in range (self.size)] for __ in range(self.size)]
        
        born_rule = rule.split('/')[0]
        survive_rule = rule.split('/')[1]

        for y in range(self.size):
            for x in range(self.size):
                
                if ( (self.board[x][y].state == False) and str(self.neighbour_matrix()[x][y]) in born_rule):
                    next_board[x][y].turn_on()
                
                elif ( (self.board[x][y].state == True) and str(self.neighbour_matrix()[x][y]) in survive_rule):
                    next_board[x][y].turn_on()
                
                else:
                    pass
            
        self.board = next_board
        self.gen += 1