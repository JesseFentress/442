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
    
    def __init__(self, board):
        self.board = board
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

    def swap(self, new_position):
        copy = cp.deepcopy(self.board)
        if new_position[0] < len(copy) and new_position[1] < len(copy[0]):
            copy[self.zero[0]][self.zero[1]] = copy[new_position[0]][new_position[1]]
            copy[new_position[0]][new_position[1]] = 0
        return copy

    def print(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(input[i][j])

    def  __eq__(self, other):
        return self.manhattan_distance == other.manhattan_distance
    
    def  __gt__(self, other):
        return self.manhattan_distance > other.manhattan_distance
    
    def __lt__(self, other):
        return self.manhattan_distance < other.manhattan_distance

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
                    used_board.append(new_board)
                    #print(new_board.manhattan_distance)
                #print(new_board.board, 'up')
            if current.zero[0] + 1 < len(current.board):
                temp_board = current.swap([current.zero[0] + 1, current.zero[1]])
                new_board = BoardState(temp_board)
                #print(new_board.hash, new_board.board)
                if new_board not in used_board:
                    priority_queue.put(new_board)
                    used_board.append(new_board)
                    #print(new_board.manhattan_distance)
                #print(new_board.board, 'down')
            if current.zero[1] - 1 >= 0:
                temp_board = current.swap([current.zero[0], current.zero[1] - 1])
                new_board = BoardState(temp_board)
                #print(new_board.hash, new_board.board)
                if new_board not in used_board:
                    priority_queue.put(new_board)
                    used_board.append(new_board)
                    #print(new_board.manhattan_distance)
                #print(new_board.board, 'left')
            if current.zero[1] + 1 < len(current.board):
                temp_board = current.swap([current.zero[0], current.zero[1] + 1])
                new_board = BoardState(temp_board)
                #print(new_board.hash, new_board.board)
                if new_board not in used_board:
                    priority_queue.put(new_board)
                    used_board.append(new_board)
                    #print(new_board.manhattan_distance)
                #print(new_board.board, 'right')
            print(used_board)

p = BoardState(input)
q = BoardState(desired_output)
print(p.hash)
print(p.manhattan_distance)
print(p.zero)
print(q.hash)
print(q.zero)
print(q.manhattan_distance)
a_star_solve(input2)