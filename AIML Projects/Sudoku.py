import heapq
from time import time
puzzle = [
    [2, 0, 0, 0],
    [0, 1, 0, 2],
    [0, 0, 3, 0],
    [0, 0, 0, 4]
]


goal_state = [
    [2, 4, 1, 3],
    [3, 1, 4, 2],
    [4, 2, 3, 1],
    [1, 3, 2, 4]
]


def heuristic(node):
    misplaced = 0
    for i in range(4):
        for j in range(4):
            if node[i][j] != goal_state[i][j]:
                misplaced += 1
    return misplaced


def is_goal(node):
    return node == goal_state


def generate_neighbors(node):
    neighbors = []
    for i in range(4):
        for j in range(4):
            if node[i][j] == 0:
                for num in range(1, 5):
                    neighbor = [row[:] for row in node]
                    neighbor[i][j] = num
                    neighbors.append(neighbor)
                return neighbors


def astar_search(start):
    open_list = [(heuristic(start), start)]
    closed_set = set()
    print("Initial state:")
    for row in puzzle:
        print(row)
    print()
    while open_list:
        _, current_node = heapq.heappop(open_list)

        if is_goal(current_node):
            return current_node

        closed_set.add(tuple(map(tuple, current_node)))

        for neighbor in generate_neighbors(current_node):
            if tuple(map(tuple, neighbor)) not in closed_set:
                g_value = 1
                f_value = g_value + heuristic(neighbor)
                print(f"cost = {f_value}")
                for row in neighbor:
                    print(row)
                print()
                heapq.heappush(open_list, (f_value, neighbor))

    return None


print('''

 $$$$$$\                  $$\           $$\                 
$$  __$$\                 $$ |          $$ |                
$$ /  \__|$$\   $$\  $$$$$$$ | $$$$$$\  $$ |  $$\ $$\   $$\ 
\$$$$$$\  $$ |  $$ |$$  __$$ |$$  __$$\ $$ | $$  |$$ |  $$ |
 \____$$\ $$ |  $$ |$$ /  $$ |$$ /  $$ |$$$$$$  / $$ |  $$ |
$$\   $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$  _$$<  $$ |  $$ |
\$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$  |$$ | \$$\ \$$$$$$  |
 \______/  \______/  \_______| \______/ \__|  \__| \______/ 

''')

start_time = time()
solution = astar_search(puzzle)
end_time = time()



Execution_time = end_time - start_time

print("Final State:")
if solution:
    for row in solution:
        print(row)
    print(f"Execution Time: {Execution_time} seconds")
else:
    print("No solution found.")
