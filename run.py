from Board import Board
from Player import Player
from AlphaBeta import best_move

DEPTH = 2

main_board = Board(Player(), Player())
main_board.draw()
while True:
    while True:
        if not main_board.ask_for_move(True):  # If method returns True player has additional move
            main_board.draw()
            break
        main_board.draw()
        print('additional move!')
    while True:
        if not main_board.player_move(False, best_move(DEPTH, main_board, False)):
            main_board.draw()
            break
        main_board.draw()
    if main_board.is_over():
        break

main_board.finish_game()
main_board.draw()
print('score: {0}'.format(main_board.get_score()))