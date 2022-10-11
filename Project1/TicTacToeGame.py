class TicTacToeGame:

    def __init__(self):
        self.board = [["-"] * 3 for i in range(3)]

    def make_player_move(self, x, y):
        if self.board[x][y] != "-":
            return False
        self.board[x][y] = "x"
        return True
    
    def make_ai_move(self, x, y):
        self.board[x][y] = "o"
        return True

    def get_board(self):
        return self.board

    def print(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                print(self.board[x][y], end="")
                if y == 0 or y < 2:
                    print(" | ", end="")
            if x == 0 or x < 2:
                print("\n---------")
        print("\n")
     
    