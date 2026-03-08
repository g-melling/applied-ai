import math
import random

def distance(a, b):
    return math.dist(a, b)

def tour_length(tour, cities):
    total = 0
    for i in range(len(tour)):
        a = cities[tour[i]]
        b = cities[tour[(i + 1) % len(tour)]]
        total += distance(a, b)
    return total

def generate_neighbors(tour, num_neighbors=50):
    neighbors = []
    n = len(tour)

    for _ in range(num_neighbors):
        i, j = random.sample(range(n), 2)
        new_tour = tour[:]
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        neighbors.append((new_tour, (i, j)))  # (solution, move)

    return neighbors

#tabu search

from collections import deque

def tabu_search_tsp(cities, iterations=500, tabu_size=20):
    n = len(cities)
    current = list(range(n))
    random.shuffle(current)

    best = current[:]
    tabu_list = deque(maxlen=tabu_size)

    for _ in range(iterations):
        neighbors = generate_neighbors(current)

        best_candidate = None
        best_candidate_cost = float("inf")
        best_move = None

        for candidate, move in neighbors:
            cost = tour_length(candidate, cities)

            if move not in tabu_list or cost < tour_length(best, cities):
                if cost < best_candidate_cost:
                    best_candidate = candidate
                    best_candidate_cost = cost
                    best_move = move

        current = best_candidate

        if tour_length(current, cities) < tour_length(best, cities):
            best = current[:]

        tabu_list.append(best_move)

    return best


if __name__ == "__main__":
    cities = [
    (0, 0), (1, 5), (5, 2), (6, 6),
    (8, 3), (2, 7), (7, 1), (3, 4)
]

best_tour = tabu_search_tsp(cities)
print("Best tour:", best_tour)
print("Tour length:", tour_length(best_tour, cities))



"""
function tabu_search():
    current = initial_solution()
    best = current
    tabu_list = empty_queue()

    for iteration in 1 to max_iterations:
        neighbors = generate_neighbors(current)

        best_candidate = None
        best_candidate_cost = infinity

        for neighbor in neighbors:
            move = move_used(current, neighbor)

            if move not in tabu_list or
               cost(neighbor) < cost(best):   // aspiration
                if cost(neighbor) < best_candidate_cost:
                    best_candidate = neighbor
                    best_candidate_cost = cost(neighbor)
                    best_move = move

        current = best_candidate

        if cost(current) < cost(best):
            best = current

        add best_move to tabu_list
        if tabu_list is too long:
            remove oldest move

    return best

"""