from collections import deque
from search_utils import reconstruct_path

def breadth_first(start, goal, cities, matrix):
    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        current_index = cities.index(current)
        for neighbor_index, distance in enumerate(matrix[current_index]):
            if distance > 0:
                neighbor = cities[neighbor_index]
                if neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = current

    return None
