import random

def group1(self, board):
    possible_moves = self.getPossibleMoves(board)
    
    if not possible_moves:
        self.game.end_turn()
        return

    best_move = None
    best_choice = None
    best_score = float('-inf')

    for move in possible_moves:
        move_score = evaluate_Move(self, board, move)

        if move_score > best_score:
            best_score = move_score
            best_move = move
            best_choice = random.choice(move[2])  

    return best_move, best_choice

def evaluate_Move(self, board, move):
    score = 0

    score += move[1] * 2  

    
    future_board = self.simulateMove(board, move)
    future_moves = len(self.getPossibleMoves(future_board))
    score += future_moves * 3  

    opponent_board = self.simulateOpponentMove(future_board)
    opponent_moves = len(self.getPossibleMoves(opponent_board))
    score -= opponent_moves * 2  

    if is_endgame(board):
        score += move[1] * 5  
    elif is_midgame(board):
        score += future_moves * 2 

    return score

def is_endgame(board):
   
    piece_count = 0

    for i in range(8):  
        for j in range(8):
            square_piece = board.getSquare(i, j).squarePiece
            if square_piece is not None:  
                piece_count += 1

    return piece_count < 10  

def is_midgame(board):
    
    piece_count = 0

    for i in range(8):  
        for j in range(8):
            square_piece = board.getSquare(i, j).squarePiece
            if square_piece is not None:  
                piece_count += 1

    return 10 <= piece_count <= 20
