import random

# Problem data
weights = [3, 9, 5, 6]
W = 18
POP_SIZE = 10
GENERATIONS = 500
MUTATION_RATE = 0.02

# Fitness function
def fitness(chromosome):
    total = sum(gene * w for gene, w in zip(chromosome, weights))
    return total if total <= W else 0

# Create random chromosome
def random_chromosome():
    return [random.randint(0, 1) for _ in range(4)]

# Roulette wheel selection
def roulette_wheel_selection(population):
    total_fitness = sum(fitness(c) for c in population)

    if total_fitness == 0:
        return random.choice(population)

    pick = random.uniform(0, total_fitness)
    current = 0

    for chromosome in population:
        current += fitness(chromosome)
        if current >= pick:
            return chromosome

# Single-point crossover
def crossover(p1, p2):
    point = random.randint(1, 3)
    return (
        p1[:point] + p2[point:],
        p2[:point] + p1[point:]
    )

# Mutation
def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]

# Initialize population
population = [random_chromosome() for _ in range(POP_SIZE)]

# GA loop
for _ in range(GENERATIONS):
    new_population = []

    while len(new_population) < POP_SIZE:
        parent1 = roulette_wheel_selection(population)
        parent2 = roulette_wheel_selection(population)

        child1, child2 = crossover(parent1, parent2)
        mutate(child1)
        mutate(child2)

        new_population.extend([child1, child2])

    population = new_population[:POP_SIZE]

# Best solution found
best = max(population, key=fitness)
print("Best solution:", best)
print("Weight:", fitness(best))
