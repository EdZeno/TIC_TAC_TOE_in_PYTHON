from lib.game import Game


def test_game_has_board():
    game = Game()
    assert game.board == [[' ',' ',' '],
                          [' ',' ',' '],
                          [' ',' ',' ']]

def test_display_board():
    game = Game()
    assert game.display_board() == '  |   |  \n–\xa0–\xa0–\xa0– -\n  |   |  \n–\xa0–\xa0–\xa0– -\n  |   |  '

def test_human_moves(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: '3')
        monkeypatch.setattr('builtins.input', lambda x: '3')
        game = Game()
        game.human_moves()
        assert game.board == [[' ',' ',' '],
                              [' ',' ',' '],
                              [' ',' ','X']]
