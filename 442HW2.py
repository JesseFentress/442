from queue import PriorityQueue

graph = {
    'A': [(1, 'B'), (5, 'E'), (2, 'C')],
    'B': [(1, 'A'), (4, 'C'), (3, 'D')],
    'C': [(8, 'D'), (3, 'E')],
    'D': [(4, 'A'), (6 ,'B')],
    'E': [(7, 'A'), (1, 'B')]
}

def uniform_cost_search(start, goal, graph):
    priority_queue = PriorityQueue()
    priority_queue.put([0, start, start])
    visited = {}
    while not priority_queue.empty():
        current = priority_queue.get()
        if current[1] == goal: # Check if goal state was reached
            return current
        for tuple in graph[current[1]]: # Adds all new paths to pq
            if tuple[1] not in visited: # Below pq entry keeps track of cost, destination, path
                priority_queue.put([tuple[0] + current[0], tuple[1], current[2]+tuple[1]]) 
        visited[current[1]] = True # Mark current as visited

print('Final Result (A -> E)', uniform_cost_search('A', 'E', graph))
print('Final Result (A -> D)', uniform_cost_search('A', 'D', graph))