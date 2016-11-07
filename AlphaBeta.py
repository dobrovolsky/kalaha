import copy


def finder(board, depth, alpha, beta, player):
    """
    alpha beta pruning algorithm
    wikipedia: http://bitly.com/2eMNdgv
    :param board: game board
    :param depth: recursion depth (count of move)
    :param alpha: minimal value
    :param beta:  maximal value
    :param player: max or min player
    :return: best state
    """
    tmp_board = copy.deepcopy(board)
    if depth == 0 or tmp_board.is_terminal():
        return tmp_board.get_score()
    if player:
        for child in tmp_board.get_children(player):
            alpha = max(alpha, finder(child, depth - 1, alpha, beta, not player))
            if beta < alpha:
                break
        return alpha
    else:
        for child in tmp_board.get_children(player):
            beta = min(beta, finder(child, depth - 1, alpha, beta, not player))
            if beta < alpha:
                break
        return beta


def best_move(depth, board, player):
    """
    Function returns best move for player
    :param depth: recursion depth (count of move)
    :param board: game board
    :param player: max or min player
    :return: best choice for board
    """
    choice = 1
    if player:
        actual_max = float('-Inf')  # best state after depth moves for max player
    else:
        actual_max = float('Inf')  # best state after depth moves for min player
    for i in range(1, 7):  # create 6 board state for next move and find best
        tmp_board = copy.deepcopy(board)
        try:
            add_move = tmp_board.player_move(player, i)
        except ValueError:
            continue
        if add_move:  # if player has additional move make biggest depth
            depth += 1
        node_score = finder(tmp_board, depth, float('-Inf'), float('Inf'), player)
        if player:
            if node_score > actual_max:
                choice = i
                actual_max = node_score
        else:
            if node_score < actual_max:
                choice = i
                actual_max = node_score
    return choice
