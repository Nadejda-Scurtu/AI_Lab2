import heapq
from search_utils import reconstruct_path

def greedy_best_first(start, goal, cities, matrix, heuristic):
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start))
    came_from = {start: None}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        current_index = cities.index(current)
        for neighbor_index, distance in enumerate(matrix[current_index]):
            if distance > 0:
                neighbor = cities[neighbor_index]
                if neighbor not in came_from:
                    came_from[neighbor] = current
                    heapq.heappush(open_set, (heuristic[neighbor], neighbor))

    return None
