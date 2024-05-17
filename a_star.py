import heapq
from search_utils import reconstruct_path

def a_star(start, goal, cities, matrix, heuristic):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {city: float('inf') for city in cities}
    g_score[start] = 0
    f_score = {city: float('inf') for city in cities}
    f_score[start] = heuristic[start]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, start, goal)

        current_index = cities.index(current)
        for neighbor_index, distance in enumerate(matrix[current_index]):
            if distance > 0:
                neighbor = cities[neighbor_index]
                tentative_g_score = g_score[current] + distance
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None
