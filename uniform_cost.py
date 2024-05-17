import heapq
from search_utils import reconstruct_path

def uniform_cost(start, goal, cities, matrix):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while open_set:
        current_cost, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        current_index = cities.index(current)
        for neighbor_index, distance in enumerate(matrix[current_index]):
            if distance > 0:
                neighbor = cities[neighbor_index]
                new_cost = current_cost + distance
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost
                    heapq.heappush(open_set, (priority, neighbor))
                    came_from[neighbor] = current

    return None
