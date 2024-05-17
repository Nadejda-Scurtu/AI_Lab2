import csv
from a_star import a_star
from breadth_first import breadth_first
from bidirectional_search import bidirectional_search
from depth_first import depth_first
from greedy_best_first import greedy_best_first
from uniform_cost import uniform_cost

# Чтение и парсинг данных
def read_map(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            cities = next(reader)
            matrix = []
            for row in reader:
                matrix.append([int(x) for x in row])
            return cities, matrix
    except Exception as e:
        print(f"Error reading the map file: {e}")
        return None, None

# Основной блок
if __name__ == "__main__":
    distance_bucharest = {
        "Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobita": 242, 
        "Eforie": 161, "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151, 
        "Iasi": 226, "Lugoj": 244, "Mehedia": 241, "Neamt": 234, 
        "Oradea": 380, "Pitesti": 100, "RM": 193, "Sibiu": 253, 
        "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374
    }

    cities, matrix = read_map('C:/Users/User/Desktop/PythonForLab/AI/Lab2/map.csv')

    if cities is not None and matrix is not None:
        start = 'Arad'
        goal = 'Bucharest'

        # Example usage
        path_a_star = a_star(start, goal, cities, matrix, distance_bucharest)
        path_breadth_first = breadth_first(start, goal, cities, matrix)
        path_bidirectional_search = bidirectional_search(start, goal, cities, matrix)
        path_depth_first = depth_first(start, goal, cities, matrix)
        path_greedy_best_first = greedy_best_first(start, goal, cities, matrix, distance_bucharest)
        path_uniform_cost = uniform_cost(start, goal, cities, matrix)

        print("A-star:", path_a_star)
        print("Breadth-first:", path_breadth_first)
        print("Bidirectional Search:", path_bidirectional_search)
        print("Depth-first:", path_depth_first)
        print("Greedy Best First:", path_greedy_best_first)
        print("Uniform Cost:", path_uniform_cost)
    else:
        print("Failed to read the map file.")
