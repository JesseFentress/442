from queue import PriorityQueue
import copy as cp

input = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 0, 11],
    [13, 14, 15, 12]
]

input3 = [
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
        self.hash = self.hash_board()

    def manhattan(self):
        manhattan_distance = 0
        goal_state = {
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
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                manhattan_distance = manhattan_distance + (abs(goal_state[self.board[i][j]][0] - i) + (abs(goal_state[self.board[i][j]][1] - j)))
        return manhattan_distance

    def find_zero(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return [i, j]

    def hash_board(self):
        idx = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                idx += self.board[i][j] * (i + len(self.board) * j)
        return idx

    def swap(self, x, y):
        copy = cp.deepcopy(self.board)
        if x < len(copy) and y < len(copy[0]):
            copy[self.zero[0]][self.zero[1]] = copy[x][y]
            copy[x][y] = 0
        return copy

    def generate_successors(self):
        successors = []
        if self.zero[0] - 1 >= 0:
            successors.append(self.swap(self.zero[0] - 1, self.zero[1]))
        if self.zero[0] + 1 < len(self.board):
            successors.append(self.swap(self.zero[0] + 1, self.zero[1]))
        if self.zero[1] - 1 >= 0:
            successors.append(self.swap(self.zero[0], self.zero[1] - 1))
        if self.zero[1] + 1 < len(self.board):
            successors.append(self.swap(self.zero[0], self.zero[1] + 1))
        return successors

    def print(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(input[i][j])

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

    def __hash__(self):
        s = set()
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                t = set({self.board[i], self.board[j], self.board[i][j]})
                s.add(t)

        return hash(s)
    

def a_star_solve(start_state):
    used_board = []
    priority_queue = PriorityQueue()
    s = BoardState(start_state)
    priority_queue.put(s)
    while not priority_queue.empty():
        current = priority_queue.get()
        print('current', current, current.manhattan_distance)
        used_board.append(current)
        print(used_board, "sd")
        if current.manhattan_distance == 0:
            print(current, 'WINNER')
            return
        else:
            if current.zero[0] - 1 >= 0:
                temp_board = current.swap([current.zero[0] - 1, current.zero[1]])
                new_board = BoardState(temp_board)
                #print(new_board.hash, new_board.board)
                if new_board not in used_board:
                    priority_queue.put(new_board)
                    
                else: 
                    print(new_board.manhattan_distance, "up")
                    #print(new_board.manhattan_distance)
                #print(new_board.board, 'up')
            if current.zero[0] + 1 < len(current.board):
                temp_board = current.swap([current.zero[0] + 1, current.zero[1]])
                new_board = BoardState(temp_board)
                #print(new_board.hash, new_board.board)
                if new_board not in used_board:
                    priority_queue.put(new_board)
                    
                    print(new_board.manhattan_distance)
                else: 
                    print(new_board.manhattan_distance, "down")
                #print(new_board.board, 'down')
            if current.zero[1] - 1 >= 0:
                temp_board = current.swap([current.zero[0], current.zero[1] - 1])
                new_board = BoardState(temp_board)
                #print(new_board.hash, new_board.board)
                if new_board not in used_board:
                    priority_queue.put(new_board)
                    
                else: 
                    print(new_board.manhattan_distance, "left")
                    #print(new_board.manhattan_distance)
                #print(new_board.board, 'left')
            if current.zero[1] + 1 < len(current.board):
                temp_board = current.swap([current.zero[0], current.zero[1] + 1])
                new_board = BoardState(temp_board)
                #print(new_board.hash, new_board.board)
                if new_board not in used_board:
                    priority_queue.put(new_board)
                    
                else: 
                    print(new_board.manhattan_distance, new_board.board, "right")
                    #print(new_board.manhattan_distance)
                #print(new_board.board, 'right')
            #print(used_board, "used")
            print(used_board, "re")

def a(start, end):
    open = []
    closed = []
    open.append(start)
    pq = PriorityQueue()
    pq.put(BoardState(start, 0))
    while not pq.empty():
        n = pq.get()
        if n.board == end:
            print("Winner", n.moves)
            return
        closed.append(n.board)
        successors = n.generate_successors()
        for child in successors:
            if child not in open and child not in closed:
                pq.put(BoardState(child, n.moves + 1))
                open.append(child)
            if child in closed and child in open:
                pass
    print("Empty")
    return



p = BoardState(input, 0)
q = BoardState(desired_output, 0)
t = BoardState(input3, 0)
print(p.hash)
print(p.manhattan_distance)
print(p.zero)
print(q.hash)
print(q.zero)
print(q.manhattan_distance)
print(t.generate_successors())
#a_star_solve(input)
a(input, desired_output)