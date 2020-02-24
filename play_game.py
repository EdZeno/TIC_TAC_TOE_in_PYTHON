from lib.game import Game

def play_game():
    game = Game()
    print(game.display_board())
    while True:
        game.human_moves()
        print(game.display_board())

        if game.winner(game.board) != None or game.draw(game.board) == 'Draw':
            break

        print('Mighty AI makes the best possible move')
        possible_moves = game.empty_cells()
        ai_choice = game.get_best_move(game.board, possible_moves, game.turns, points=[])
        game.ai_moves(ai_choice)
        print(game.display_board())

        if game.winner(game.board) != None or game.draw(game.board) == 'Draw':
            break



play_game()
