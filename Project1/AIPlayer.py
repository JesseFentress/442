import sys
import copy as cp

class AIPlayer:

    def valid_win(self, a, b, c):
        # A win is confirmed if the three given values are equal
        return a == b and b == c and a != "-"

    def check_winner(self, board):
        winner = None # Holds winner of the current board state
        for row in range(3): # Checks for horizontal wins
            if self.valid_win(board[row][0], board[row][1], board[row][2]):
                winner = board[row][0] # Winner
        for col in range(3): # Checks for vertical wins
            if self.valid_win(board[0][col], board[1][col], board[2][col]):
                winner = board[0][col]
        # Checks for diagonal win
        if self.valid_win(board[0][0], board[1][1], board[2][2]):
            winner = board[0][0] # Winner
        # Checks for diagonal win
        if self.valid_win(board[2][0], board[1][1], board[0][2]):
            winner = board[2][0] # Winner
        available_moves = 0 # Hold number of available moves
        for row in range(3):
            for col in range(3):
                # If the has not been selected
                if board[row][col] == "-":
                    #Increment number of available moves
                    available_moves = available_moves + 1
        # If there is no winner and no available moves
        if available_moves == 0 and winner == None: 
            return "tie"
        else: # There is a winner
            return winner

    def minimax(self, board, depth, is_maximizing_player):  
        scores = {"o": 10, "x": -10, "tie": 0} # Scores based on winner
        winner = self.check_winner(board) # Find winner of the board
        if winner != None: # If there is a winner
            return scores[winner] # Return the score of the winner
        if is_maximizing_player: # If this is the max player (AI)
            best_score = -sys.maxsize # Best score starts at -infinity for AI
            for row in range(3):
                for col in range(3):
                    if board[row][col] == "-": # Spot is available
                        board[row][col] = "o" # Alter the spot to AI move
                        # Minimax score of altered board
                        move_score = self.minimax(board, depth + 1, not is_maximizing_player)
                        board[row][col] == "-" # Alter the spot back to available
                        best_score = max(move_score, best_score) # Max score 
            return best_score # Return best score
        else: # If this the min player (Human)
            best_score = sys.maxsize # Best score starts at infinity for human
            for row in range(3):
                for col in range(3):
                    if board[row][col] == "-": # Spot is available
                        board[row][col] = "x" # Alter the spot to Human move
                        # Minimax score of altered board
                        move_score = self.minimax(board, depth + 1, not is_maximizing_player)
                        board[row][col] == "-" # Alter the spot back to available
                        best_score = min(move_score, best_score) # Min score
            return best_score # Return best score

    def make_move(self, board, algorithm="mm"):
        if algorithm =="ab":
            copy = cp.deepcopy(board) # Make a copy of the board
            best_score = -sys.maxsize # Best score starts at -infinity
            move = {} # Holds the best move for the AI
            for row in range(3):
                for col in range(3):
                    if board[row][col] == "-": # If the spot is available
                        copy[row][col] = "o" # Alter the spot to AI move
                        score = self.alpha_beta(copy, 0, False, -2, 2) # Minimax the board
                        copy[row][col] = "-" # Alter the spot back to available
                        if score > best_score: # Minimax score is better than current
                            best_score = score # Update best score
                            move["row"] = row # Save the row
                            move["col"] = col # Save the column
            return move # Return the best move
        copy = cp.deepcopy(board) # Make a copy of the board
        best_score = -sys.maxsize # Best score starts at -infinity
        move = {} # Holds the best move for the AI
        for row in range(3):
            for col in range(3):
                if board[row][col] == "-": # If the spot is available
                    copy[row][col] = "o" # Alter the spot to AI move
                    score = self.minimax(copy, 0, False) # Minimax the board
                    copy[row][col] = "-" # Alter the spot back to available
                    if score > best_score: # Minimax score is better than current
                        best_score = score # Update best score
                        move["row"] = row # Save the row
                        move["col"] = col # Save the column
        return move # Return the best move
        
    def alpha_beta(self, board, depth, is_maximizing_player, alpha, beta):
        scores = {"o": 10, "x": -10, "tie": 0} # Scores based on winner
        winner = self.check_winner(board) # Find winner of the board
        if winner != None: # If there is a winner
            return scores[winner] # Return the score of the winner
        if is_maximizing_player: # If this is the max player (AI)
            best_score = -sys.maxsize # Best score starts at -infinity for AI
            for row in range(3):
                for col in range(3):
                    if board[row][col] == "-": # Spot is available
                        board[row][col] = "o" # Alter the spot to AI move
                        # Minimax score of altered board
                        move_score = self.alpha_beta(board, depth + 1, not is_maximizing_player, alpha, beta)
                        if move_score > best_score:
                            best_score = move_score
                        board[row][col] == "-" # Alter the spot back to available
                        if best_score >= beta:
                            return best_score
                        if best_score > alpha:
                            alpha = best_score
            return best_score # Return best score
        else: # If this the min player (Human)
            best_score = sys.maxsize # Best score starts at infinity for human
            for row in range(3):
                for col in range(3):
                    if board[row][col] == "-": # Spot is available
                        board[row][col] = "x" # Alter the spot to Human move
                        # Minimax score of altered board
                        move_score = self.alpha_beta(board, depth + 1, not is_maximizing_player, alpha, beta)
                        if move_score < best_score:
                            best_score = move_score
                        board[row][col] == "-" # Alter the spot back to available
                        if best_score <= alpha:
                            return best_score
                        if best_score < beta:
                            beta = best_score
            return best_score # Return best score