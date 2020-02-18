from lib.game import Game

def test_game_has_board():
    game = Game()
    assert game.board == [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def test_display_board():
    game = Game()
    assert game.display_board() == '  |   |  \n– – – – -\n  |   |  \n– – – – -\n  |   |  '

def test_human_moves(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: '3')
        monkeypatch.setattr('builtins.input', lambda x: '3')
        game = Game()
        game.human_moves()
        assert game.board == [[' ',' ',' '],[' ',' ',' '],[' ',' ','X']]

def test_winner_horizontal():
    game = Game()
    board = [['X','X','X'],[' ',' ',' '],[' ',' ',' ']]
    assert game.winner(board) == 'X'

def test_winner_horizontal_none():
    game = Game()
    board = [['X','X',' '],[' ',' ',' '],[' ',' ',' ']]
    assert game.winner(board) == None

def test_winner_horizontal_second():
    game = Game()
    board = [[' ',' ',' '],['O','O','O'],[' ',' ',' ']]
    assert game.winner(board) == 'O'

def test_winner_horizontal_third():
    game = Game()
    board = [[' ',' ',' '],[' ',' ',' '],['X','X','X']]
    assert game.winner(board) == 'X'

def test_winner_vertical():
    game = Game()
    board = [['O',' ',' '],['O',' ',' '],['O',' ',' ']]
    assert game.winner(board) == 'O'

def test_winner_vertical_second():
    game = Game()
    board = [[' ','O',' '],[' ','O',' '],[' ','O',' ']]
    assert game.winner(board) == 'O'

def test_winner_vertical_third():
    game = Game()
    board = [[' ',' ','O'],[' ',' ','O'],[' ',' ','O']]
    assert game.winner(board) == 'O'

def test_winner_vertical_fourth():
    game = Game()
    board = [[' ',' ','O'],[' ',' ','O'],[' ',' ',' ']]
    assert game.winner(board) == None

def test_winner_diagonal():
    game = Game()
    board = [['O',' ',' '],[' ','O',' '],[' ',' ','O']]
    assert game.winner(board) == 'O'

def test_winner_diagonal_second():
    game = Game()
    board = [[' ',' ','O'],[' ','O',' '],['O',' ',' ']]
    assert game.winner(board) == 'O'

def test_draw():
    game = Game()
    board = [['X','X','O'],['O','O','X'],['X','O','O']]
    assert game.draw(board) == 'Draw'

def test_draw_fail():
    game = Game()
    board = [['X','X','O'],['O','O',' '],['X','O','O']]
    assert game.draw(board) == 'Make your move'

def test_draw_second():
    game = Game()
    board = [['O','X','X'],['X','O','O'],['O','O','X']]
    assert game.draw(board) == 'Draw'

def test_empty_cells():
    game = Game()
    board = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]
    assert game.empty_cells(board) == [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

def test_empty_cells_one_element():
    game = Game()
    board = [[' ',' ',' '],
             [' ','X',' '],
             [' ',' ',' ']]
    assert game.empty_cells(board) == [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]

def test_empty_cells_three_element():
    game = Game()
    board = [[' ',' ',' '],
             ['X','X','O'],
             [' ',' ',' ']]
    assert game.empty_cells(board) == [[0,0],[0,1],[0,2],[2,0],[2,1],[2,2]]

def test_get_best_move_second():
    empty_cells = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    board = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]
    turns = ['X']
    game = Game()
    points = game.get_best_move(board, empty_cells, turns, points=[])
    assert  len(points) == 255168
