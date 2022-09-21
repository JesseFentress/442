from queue import PriorityQueue
import copy as cp

input = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 0, 11],
    [13, 14, 15, 12]
]

input2 = [
    [1, 3, 6, 4],
    [5, 2, 0, 8],
    [10, 9, 7, 11],
    [14, 15, 13, 12]
]

desired_output = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]

class BoardState:
    
    def __init__(self, board, moves):
        self.board = board 
        self.moves = moves
        self.manhattan_distance = self.manhattan()
        self.zero = self.find_zero()

    def manhattan(self):
        manhattan_distance = 0 # Starting manhattan distance
        goal_state = { # Dictionary that holds goal position for each number
            1: [0,0],
            2: [0,1],
            3: [0,2],
            4: [0,3],
            5: [1,0],
            6: [1,1],
            7: [1,2],
            8: [1,3],
            9: [2,0],
            10: [2,1],
            11: [2,2],
            12: [2,3],
            13: [3,0],
            14: [3,1],
            15: [3,2],
            0: [3, 3]
        }
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                # Finding manhattan distance can be done by summing the distance (the difference) 
                # from the current position of a number and its goal position (x and y position)
                manhattan_distance = manhattan_distance + (abs(goal_state[self.board[x][y]][0] - y) + (abs(goal_state[self.board[x][y]][1] - y)))
        return manhattan_distance

    def find_zero(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 0:
                    return [x, y] # Keeps track of a board's zero (or empty) location

    def swap(self, x, y):
        copy = cp.deepcopy(self.board) # Makes a copy of the board 
        if x < len(copy) and y < len(copy[0]):
            # Swapping zero (or empty) node with some adjacent node
            copy[self.zero[0]][self.zero[1]] = copy[x][y]
            copy[x][y] = 0
        return copy

    def generate_successors(self):
        successors = []
        if self.zero[0] - 1 >= 0: # Swap with above adjacent node
            successors.append(self.swap(self.zero[0] - 1, self.zero[1]))
        if self.zero[0] + 1 < len(self.board): # Swap with below adjacent node
            successors.append(self.swap(self.zero[0] + 1, self.zero[1]))
        if self.zero[1] - 1 >= 0: # Swap with left adjacent node
            successors.append(self.swap(self.zero[0], self.zero[1] - 1))
        if self.zero[1] + 1 < len(self.board): # Swap with right adjacent node
            successors.append(self.swap(self.zero[0], self.zero[1] + 1))
        return successors

    def print(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(str(input[i][j]))
            print("\n")

    def  __eq__(self, other):
        return self.manhattan_distance + self.moves == other.manhattan_distance + other.moves and self.board == other.board
    
    def  __gt__(self, other):
        return self.manhattan_distance + self.moves > other.manhattan_distance + other.moves
    
    def __ge__(self, other):
        return self.manhattan_distance + self.moves >= other.manhattan_distance + other.moves
    
    def __le__(self, other):
        return self.manhattan_distance + self.moves <= other.manhattan_distance + other.moves
    
    def __lt__(self, other):
        return self.manhattan_distance + self.moves < other.manhattan_distance + other.moves 

    def __repr__(self):
        return str(self.board)

    def __str__(self):
        return str(self.board)

def a(start, end):
    open = [] 
    closed = []
    open.append(start) # Adds start board to open list
    pq = PriorityQueue() # Used for returning lowest g(n) + h(n) board
    pq.put(BoardState(start, 0)) # Add start board to pq
    while not pq.empty():
        n = pq.get() # Get the most desirable board (lowest g(n) + h(n))
        print(n) # Print the board
        if n.board == end: # Goal was reached
            print("Goal Reached in " + str(n.moves) + " moves.")
            return
        closed.append(n.board) # Add the current board to the closed list
        successors = n.generate_successors() # Gets an array of successor boards
        for child in successors:
            if child not in open and child not in closed:
                pq.put(BoardState(child, n.moves + 1)) # Add new board to pq
                open.append(child) # Add new board to open list
    print("No possible solution")
    return



#p = BoardState(input, 0)
#q = BoardState(desired_output, 0)
#t = BoardState(input3, 0)
#print(p.hash)
#print(p.manhattan_distance)
#print(p.zero)
#print(q.hash)
#print(q.zero)
#print(q.manhattan_distance)
#print(t.generate_successors())
#a_star_solve(input)
a(input, desired_output)
