import copy

class Board():
    def __init__(self, board = None):
        if board == None:
            self.board = [[ ' ' for c in range(3)] for r in range(3)]
            self.current_symbol = 'X'
            self.score = 100
            self.move_r =None
            self.move_c= None
            self.children=[]
        else:
            self.board = copy.deepcopy(board.board)
            self.current_symbol = board.current_symbol
            self.score = board.score
            self.move_r = board.move_r
            self.move_c = board.move_c
            self.children = board.children

    def check_win(self):
        if (self.check_col_win('X')):
            self.score=1
            return True
        
        if (self.check_col_win('O')):
            self.score = -1
            return True

        if (self.check_row_win('X')):
            self.score =1
            return True
        
        if (self.check_row_win('O')):
            self.score =-1
            return True

        if (self.check_diagnol_win('X')):
            self.score = 1
            return True
            
        if (self.check_diagnol_win('O')):
            self.score = -1
            return True

        if (self.check_draw()):
            self.score = 0
            return True
        else:
            return False
        
        

    def check_col_win(self, symbol):
        for c in range(0,3):
            if self.board[0][c] == symbol and self.board[1][c] == symbol and  self.board[2][c]==symbol:
                return True
        return False

    def check_row_win(self, symbol):
        for r in range(0,3):
            if self.board[r][0] == symbol and self.board[r][1] == symbol and  self.board[r][2]==symbol:
                return True
        return False

    def check_diagnol_win(self,symbol):
        if self.board[0][0] == symbol and self.board[1][1] == symbol and  self.board[2][2]==symbol:
            return True
        elif self.board[2][0] == symbol and self.board[1][1] == symbol and  self.board[0][2]==symbol:
            return True
        else:
            return False

    def check_draw(self):
        placed_pieces = 0
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 'X' or self.board[r][c] =='O':
                    placed_pieces = placed_pieces + 1
        
        if placed_pieces == 9:
            return True
        else:
            return False

    def print_board(self):
        for r in range(3):
            for c in range(3):
                if c == 2:
                    print(" " + str(self.board[r][c]))
                else:
                    print(" " +str(self.board[r][c])+" :", end="")
            
            if r <2:
                print("----------")
            else:
                print()
    def swap_symbol(self):
        if self.current_symbol =='X':
            self.current_symbol = 'O'
        else:
            self.current_symbol = 'X'
        

    def get_next_states(self):
        states=[]
        for r in range(3):
            for c in range(3):
                if self.board[r][c]==' ':
                    new_board = Board(self)
                    new_board.make_move(r,c,self.current_symbol)
                    new_board.swap_symbol()
                    states.append(new_board)
        self.children = states
        return states
        
    def make_move(self,r,c, symbol):
        self.board[r][c] = symbol
        self.move_r=r
        self.move_c=c
        return self

    
def min_max(board):
    #print("in min max")
  #  print("current Symbol", board.current_symbol)
  #  print("current board")
    #board.print_board()
    max = -1
    min = 1
    states= board.get_next_states()
    
    if board.current_symbol == 'X':
      #  print("Going for max")
        while len(states) > 0:
            check_state = states.pop()
            game_over = check_state.check_win()
            if game_over:
             #   print("GAMEOVER", check_state.score)
             #   check_state.print_board()
             #   print("MOVE", check_state.move_r, check_state.move_c)
                return check_state.score, check_state.move_r, check_state.move_c
            else:

                temp, move_r, move_c = min_max(check_state) 
                if temp <100 and temp > max:    
                   # print("new max")
                    board.score = temp
                    max = temp
                else:
                    pass
        #            print("no new max")
       #         print("OUT OF MAX")
           
        #    check_state.print_board()
        #    print(check_state.score)
        #    print()
    else:
      #  print("going for min")
        while len(states) > 0:
            check_state = states.pop()
            game_over = check_state.check_win()
            if game_over:
         #       print("GAMEOVER", check_state.score)
              #  check_state.print_board()
               # print("MOVE", check_state.move_r, check_state.move_c)
                return check_state.score, check_state.move_r, check_state.move_c
            else:

                temp, move_r, move_c = min_max(check_state) 
                if temp <100 and temp < min:    
                   # print("new min", temp)
                    board.score = temp
                    min = temp
                else:
                    pass
     #               print("no new min")
     #           print("OUT OF MIN")

    #print("DONE", board.score, move_r, move_c)
    return board.score, move_r, move_c
   # board.print_board()

  #  for s in states:
  #      s.print_board()
  #      print("score", s.score)
    


b = Board()

class AIPlayer:
    def __init__(self):
        self.states=[]
    
    def make_move(self,board):
        board.print_board()
        score, r,c =    min_max(board)
        new_board = board.make_move(r,c,board.current_symbol)
        #print("SCORE:", score, r,c)
        new_board.swap_symbol()
        new_board.print_board()
        return new_board.check_win(), new_board

ai = AIPlayer()
gameover = False
while not gameover:

    gameover, b = ai.make_move(b)
#b.print_board()
#b.make_move(0,0,'X')
#b.print_board()
#b.make_move(0,1,'O')
#b.print_board()

#c=Board(b)

#c.print_board()

#print()
#print()

#c.make_move(1,1,'X')
#c.print_board()
#b.print_board()

