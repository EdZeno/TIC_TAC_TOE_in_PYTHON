import copy

class Game():
    board = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]

    tunrs = []

    def display_board(self):
      board_copy = self.board.copy()
      board_copy.insert(1, ['– – – – -'])
      board_copy.insert(3, ['– – – – -'])
      pretty_board = ''.join('\n'.join([' | '.join([str(elem) for elem in list]) for list in board_copy]))
      print(pretty_board)
      return pretty_board

    def human_moves(self):
      row = input("Drawing an X\nSelect a row  1-3 (from top to buttom)  ")
      cell = input("Select a cell 1-3 (from left to right)  ")
      self.board[int(row)-1][int(cell)-1]="X"
      return print(self.display_board())

    def winner(self, board):
      for i in [0,1,2]:
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != ' '):
          return board[i][0]
        elif (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != ' '):
          return board[0][i]

      if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' '):
        return board[0][0]
      elif (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != ' '):
        return board[2][0]

    def draw(self, board):
        moves = []
        print(moves)
        for i in board:
            if ' ' in i:
                moves.append(1)
        print(moves)
        if self.winner(board) == None and len(moves) == 0:
            return 'Draw'
        else:
            return 'Make your move'

    def empty_cells(self):
        empty_cells = [[index1,index2] for index1,value1 in enumerate(self.board) for index2,value2 in enumerate(value1) if value2==' ']
        return empty_cells

    def get_best_move(self, board, empty_cells, turns, points=[]):

        for cell in empty_cells:
            new_board = copy.deepcopy(board)
            new_turns = turns.copy()
            # print('START')
            # print(board)
            if turns[-1] == 'X':
              new_board[cell[0]][cell[1]] = 'O'
              new_turns.append('O')
            elif turns[-1] == 'O':
              new_board[cell[0]][cell[1]] = 'X'
              new_turns.append('X')

            new_empty_cells = [[index1,index2] for index1,value1 in enumerate(new_board) for index2,value2 in enumerate(value1) if value2==' ']
            # print(new_board)
            # print(new_empty_cells)
            if self.winner(new_board) == 'X':
              points.append(-1)
            elif self.winner(new_board) == 'O':
              points.append(1)
            elif len(new_empty_cells) == 0:
              points.append(0)
            else:
              self.get_best_move(new_board, new_empty_cells, new_turns, points)
        return points

    def ai_moves(self, points):
        empty_cells = [[index1,index2] for index1,value1 in enumerate(self.board) for index2,value2 in enumerate(value1) if value2==' ']
        divisor = len(points) // len(empty_cells)
        nested = [points[i:i+divisor] for i in range(0, len(points), divisor)]
        sums = [sum(value) for value in nested]
        best_move = sums.index(max(sums))
        self.board[empty_cells[best_move][0]][empty_cells[best_move][1]] = "O"
        return self.board[empty_cells[best_move][0]][empty_cells[best_move][1]]
