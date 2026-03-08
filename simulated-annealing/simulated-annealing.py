import math
import random

# Objective function
def cost(x):
    return x**2 + 10 * math.sin(x)

# Simulated Annealing
def simulated_annealing():
    x = random.uniform(-10, 10)   # initial solution
    best_x = x

    T = 100.0                     # initial temperature
    T_min = 0.001
    alpha = 0.95                  # cooling rate

    while T > T_min:
        # small random step
        x_new = x + random.uniform(-1, 1)

        delta = cost(x_new) - cost(x)

        if delta <= 0:
            x = x_new
        else:
            prob = math.exp(-delta / T)
            if random.random() < prob:
                x = x_new

        if cost(x) < cost(best_x):
            best_x = x

        T *= alpha

    return best_x

result = simulated_annealing()
print("Best x:", result)
print("Cost:", cost(result))


"""
function simulated_annealing():
    current = random_solution()
    best = current
    T = initial_temperature

    while T > minimum_temperature:
        neighbor = small_random_change(current)
        Δ = cost(neighbor) - cost(current)

        if Δ <= 0:
            current = neighbor
        else:
            accept_prob = exp(-Δ / T)
            if random(0,1) < accept_prob:
                current = neighbor

        if cost(current) < cost(best):
            best = current

        T = cooling_rate * T

    return best

"""