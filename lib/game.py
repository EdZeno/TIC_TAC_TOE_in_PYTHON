import copy

class Game():
    # board = [[' ',' ',' '],
    #          [' ',' ',' '],
    #          [' ',' ',' ']]

    board = [[' ',' '],
             [' ',' ']]

    def display_board(self):
      board_copy = self.board.copy()
      board_copy.insert(1, ['– – – – -'])
      board_copy.insert(3, ['– – – – -'])
      pretty_board = ''.join('\n'.join([' | '.join([str(elem) for elem in list]) for list in board_copy]))
      return pretty_board

    def human_moves(self):
      row = input("Drawing an X\nSelect a row  1-3 (from top to buttom)  ")
      cell = input("Select a cell 1-3 (from left to right)  ")
      self.board[int(row)-1][int(cell)-1]="X"
      return print(self.display_board())


    def trial(self, board, empty_cells, turns):
        for cell in empty_cells:
            new_board = copy.deepcopy(board)
            new_turns = turns.copy()
            print('START')
            print(board)
            if turns[-1] == 'X':
              new_board[cell[0]][cell[1]] = 'O'
              new_turns.append('O')
            elif turns[-1] == 'O':
              new_board[cell[0]][cell[1]] = 'X'
              new_turns.append('X')

            new_empty_cells = [[index1,index2] for index1,value1 in enumerate(new_board) for index2,value2 in enumerate(value1) if value2==' ']
            print('--------')
            print(new_board)
            print('--------')
            print(new_empty_cells)
            if len(new_empty_cells) == 0:
                return 'I am out of here'
            else:
                self.trial(new_board, new_empty_cells, new_turns)
