from AIPlayer import AIPlayer

class GamePlayer:

    def __init__(self, game):
        self.game = game
        self.AI = AIPlayer()

    def play_minimax(self):
        print("\nWelcome to Tic Tac Toe (Minimax)")
        print("The AI will perform the first move.")
        while not self.is_game_over():
            # AI makes a move
            ai_move = self.AI.make_move(self.game.board)
            # AI's move is performed on the board
            self.game.make_ai_move(ai_move["row"], ai_move["col"])
            # Check if the game is over
            if self.is_game_over():
                break
            print("\nMake a move (choose an x and y position):")
            self.game.print()
            # Take input for the User's move
            x_input = input("Row: ")
            y_input = input("Column: ")
            # Quit the game if the user wants to
            if x_input == "q" or y_input == "q":
                break
            # Perform the User's move on the board and tell them to make
            # a new move if it is invalid
            if not self.game.make_player_move(int(x_input), int(y_input)):
                print("\nInvalid move, please make another:")
                self.game.print()
                x_input = input("Row: ")
                y_input = input("Column: ")

    def play_minimax_help(self):
        print("\nWelcome to Tic Tac Toe (Minimax with help)")
        print("The AI will perform the first move.")
        while not self.is_game_over():
            # AI makes a move
            ai_move = self.AI.make_move(self.game.board)
            # AI's move is performed on the board
            self.game.make_ai_move(ai_move["row"], ai_move["col"])
            # Check if the game is over
            if self.is_game_over():
                break
            # Find optimal move for the User
            om = self.AI.make_move(self.game.board)
            print("\nYour optimal move would be: " + str(om))
            print("\nMake a move (choose an x and y position):")
            self.game.print()
            # Take input for the User's move
            x_input = input("Row: ")
            y_input = input("Column: ")
            # Quit the game if the user wants to
            if x_input == "q" or y_input == "q":
                break
            # Perform the User's move on the board and tell them to make
            # a new move if it is invalid
            if not self.game.make_player_move(int(x_input), int(y_input)):
                print("\nInvalid move, please make another:")
                self.game.print()
                x_input = input("Row: ")
                y_input = input("Column: ")

    def play_alpha_beta(self):
        print("\nWelcome to Tic Tac Toe (Alpha-Beta)")
        print("The AI will perform the first move.")
        while not self.is_game_over():
            # AI makes a move
            ai_move = self.AI.make_move(self.game.board, "ab")
            # AI's move is performed on the board
            self.game.make_ai_move(ai_move["row"], ai_move["col"])
            # Check if the game is over
            if self.is_game_over():
                break
            print("\nMake a move (choose an x and y position):")
            self.game.print()
            # Take input for the User's move
            x_input = input("Row: ")
            y_input = input("Column: ")
            # Quit the game if the user wants to
            if x_input == "q" or y_input == "q":
                break
            # Perform the User's move on the board and tell them to make
            # a new move if it is invalid
            if not self.game.make_player_move(int(x_input), int(y_input)):
                print("\nInvalid move, please make another:")
                self.game.print()
                x_input = input("Row: ")
                y_input = input("Column: ")

    def play_alpha_beta_help(self):
        print("\nWelcome to Tic Tac Toe (Alpha-Beta)")
        print("The AI will perform the first move.")
        while not self.is_game_over():
            # AI makes a move
            ai_move = self.AI.make_move(self.game.board, "ab")
            # AI's move is performed on the board
            self.game.make_ai_move(ai_move["row"], ai_move["col"])
            # Check if the game is over
            if self.is_game_over():
                break
            # Find optimal move for the User
            optimal_move = self.AI.make_move(self.game.board, "a")
            print("\nYour optimal move would be: " + str(optimal_move))
            print("\nMake a move (choose an x and y position):")
            self.game.print()
            # Take input for the User's move
            x_input = input("Row: ")
            y_input = input("Column: ")
            # Quit the game if the user wants to
            if x_input == "q" or y_input == "q":
                break
            # Perform the User's move on the board and tell them to make
            # a new move if it is invalid
            if not self.game.make_player_move(int(x_input), int(y_input)):
                print("\nInvalid move, please make another:")
                self.game.print()
                x_input = input("Row: ")
                y_input = input("Column: ")

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

    def is_game_over(self):
        game_over_message = {
            "x": "Game Over! You have won!",
            "o": "Game Over! The AI has won!",
            "tie": "Game Over! It's a tie!"
        } 
        # Check for a winner
        winner = self.check_winner(self.game.board)
        # No winner so return False
        if not winner:
            return False
        self.game.print()
        print(game_over_message[winner])
        # There is a winner so return True
        return True


