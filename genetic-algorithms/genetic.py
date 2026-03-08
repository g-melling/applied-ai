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

# Tournament selection
def tournament_selection(pop):
    a, b = random.sample(pop, 2)
    return a if fitness(a) > fitness(b) else b

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
        p1 = tournament_selection(population)
        p2 = tournament_selection(population)
        c1, c2 = crossover(p1, p2)
        mutate(c1)
        mutate(c2)
        new_population.extend([c1, c2])
    population = new_population[:POP_SIZE]

# Best solution
best = max(population, key=fitness)
print("Best solution:", best)

print("Weight:", fitness(best))


"""
Initialize population randomly

repeat for N generations:
    evaluate fitness of each chromosome

    new_population = []

    while new_population size < population size:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)

        child1, child2 = crossover(parent1, parent2)

        mutate(child1)
        mutate(child2)

        add children to new_population

    population = new_population

return best solution found
"""
