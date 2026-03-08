import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # macOS-compatible backend
import matplotlib.pyplot as plt

# -------------------------
# Random initial solution
# -------------------------
def random_solution(tsp):
    cities = list(range(len(tsp)))
    random.shuffle(cities)
    return cities

# -------------------------
# Generate neighbors by swapping adjacent cities
# -------------------------
def get_neighbours(solution):
    neighbours = []
    for i in range(len(solution)-1):
        neighbour = solution.copy()
        neighbour[i], neighbour[i+1] = neighbour[i+1], neighbour[i]
        neighbours.append(neighbour)
    return neighbours

# -------------------------
# Compute total route length
# -------------------------
def route_length(tsp, solution):
    length = 0
    for i in range(len(solution)):
        length += tsp[solution[i-1]][solution[i]]  # wrap around to last city
    return length

# -------------------------
# Simple Hill Climbing
# -------------------------
def simple_hill_climbing(tsp, max_no_improve=25):
    current_solution = random_solution(tsp)
    current_length = route_length(tsp, current_solution)
    no_improve_count = 0

    iteration_lengths = [current_length]

    while no_improve_count < max_no_improve:
        moved = False
        neighbours = get_neighbours(current_solution)

        # Move to the first neighbor that improves the route
        for neighbour in neighbours:
            neighbour_length = route_length(tsp, neighbour)
            if neighbour_length < current_length:
                current_solution = neighbour
                current_length = neighbour_length
                moved = True
                break  # move immediately to first improvement

        if moved:
            no_improve_count = 0
        else:
            no_improve_count += 1

        iteration_lengths.append(current_length)

    return current_solution, current_length, iteration_lengths

# -------------------------
# Main: Run 10 times and plot
# -------------------------
def main():
    # Load TSP distance matrix
    tsp = []
    with open("TSP-Matrix-1.txt") as f:
        for line in f:
            tsp.append(list(map(int, line.strip().split(","))))

    all_iteration_lengths = []
    all_solutions = []

    best_length_overall = float('inf')
    best_solution_overall = None
    best_iteration_lengths = []

    for run in range(10):
        random.seed(None)  # ensure different random start each run
        solution, length, iteration_lengths = simple_hill_climbing(tsp)
        all_iteration_lengths.append(iteration_lengths)
        all_solutions.append(solution)

        print(f"Run {run+1}: Best Length = {length}")

        # Track best overall
        if length < best_length_overall:
            best_length_overall = length
            best_solution_overall = solution
            best_iteration_lengths = iteration_lengths

    print("\n=== Best Run Overall ===")
    print("Best Route Length:", best_length_overall)
    print("Tour of Cities Visited (indices):", best_solution_overall)

    # Pad all runs to same length for plotting
    max_iters = max(len(l) for l in all_iteration_lengths)
    padded_lengths = []
    for l in all_iteration_lengths:
        padded = l + [l[-1]]*(max_iters - len(l))
        padded_lengths.append(padded)

    # -------------------------
    # Plot all runs
    # -------------------------
    plt.figure(figsize=(10,6))
    for i, run_lengths in enumerate(padded_lengths):
        plt.plot(range(len(run_lengths)), run_lengths, marker='o', label=f'Run {i+1}')
    
    # Highlight best run
    plt.plot(range(len(best_iteration_lengths)), best_iteration_lengths,
             'r-', linewidth=3, label='Best Run')

    plt.xlabel("Iteration")
    plt.ylabel("Route Length")
    plt.title("Simple Hill Climbing: Cost vs Iteration (10 Runs)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
