"""
function simulated_annealing_TSP(cities):
    current_tour = random_permutation(cities)
    best_tour = current_tour
    T = initial_temperature

    while T > minimum_temperature:
        new_tour = swap_two_cities(current_tour)

        Δ = distance(new_tour) - distance(current_tour)

        if Δ <= 0:
            current_tour = new_tour
        else:
            if random(0,1) < exp(-Δ / T):
                current_tour = new_tour

        if distance(current_tour) < distance(best_tour):
            best_tour = current_tour

        T = cooling_rate * T

    return best_tour
"""

import math
import random

def distance(city1, city2):
    return math.dist(city1, city2)

def tour_length(tour, cities):
    total = 0
    for i in range(len(tour)):
        city_a = cities[tour[i]]
        city_b = cities[tour[(i + 1) % len(tour)]]
        total += distance(city_a, city_b)
    return total

def swap_two_cities(tour):
    new_tour = tour[:]
    i, j = random.sample(range(len(tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

def simulated_annealing_tsp(cities):
    n = len(cities)
    current_tour = list(range(n))
    random.shuffle(current_tour)

    best_tour = current_tour[:]

    T = 1000.0
    T_min = 0.001
    alpha = 0.995

    while T > T_min:
        new_tour = swap_two_cities(current_tour)

        delta = (tour_length(new_tour, cities)
                 - tour_length(current_tour, cities))

        if delta <= 0:
            current_tour = new_tour
        else:
            prob = math.exp(-delta / T)
            if random.random() < prob:
                current_tour = new_tour

        if tour_length(current_tour, cities) < tour_length(best_tour, cities):
            best_tour = current_tour[:]

        T *= alpha

    return best_tour


if __name__ == "__main__":
    # Example cities (x, y)
    cities = [
        (0, 0), (1, 5), (5, 2), (6, 6),
        (8, 3), (2, 7), (7, 1), (3, 4)
    ]

    best_tour = simulated_annealing_tsp(cities)
    print("Best tour:", best_tour)
    print("Tour length:", tour_length(best_tour, cities))

