from collections import deque
from search_utils import reconstruct_path

def bidirectional_search(start, goal, cities, matrix):
    if start == goal:
        return [start]

    def bfs(frontier, visited, parents, other_parents):
        current = frontier.popleft()
        current_index = cities.index(current)

        for neighbor_index, distance in enumerate(matrix[current_index]):
            if distance > 0:
                neighbor = cities[neighbor_index]
                if neighbor not in visited:
                    frontier.append(neighbor)
                    visited.add(neighbor)
                    parents[neighbor] = current
                    if neighbor in other_parents:
                        return neighbor
        return None

    start_frontier = deque([start])
    goal_frontier = deque([goal])
    start_visited = {start}
    goal_visited = {goal}
    start_parents = {start: None}
    goal_parents = {goal: None}

    while start_frontier and goal_frontier:
        intersection = bfs(start_frontier, start_visited, start_parents, goal_parents)
        if intersection:
            path_from_start = reconstruct_path(start_parents, start, intersection)
            path_from_goal = reconstruct_path(goal_parents, goal, intersection)
            return path_from_start[:-1] + path_from_goal[::-1]

        intersection = bfs(goal_frontier, goal_visited, goal_parents, start_parents)
        if intersection:
            path_from_start = reconstruct_path(start_parents, start, intersection)
            path_from_goal = reconstruct_path(goal_parents, goal, intersection)
            return path_from_start[:-1] + path_from_goal[::-1]

    return None
