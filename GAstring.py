import random
import string

def genetic_algorithm(target):
    def random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

    def fitness(candidate):
        match_count = 0
        for i in range(len(target)):
            if target[i] == candidate[i]:
                match_count += 1
        return match_count

    def select(population):
        weights = [fitness(c) for c in population]
        return random.choices(population, weights, k=2)

    def crossover(p1, p2):
        point = random.randint(1, len(p1) - 1)
        return p1[:point] + p2[point:]

    def mutate(candidate):
        candidate = list(candidate)
        for i in range(len(candidate)):
            if random.random() < 0.01:
                candidate[i] = random.choice(string.ascii_lowercase)
        return ''.join(candidate)

    population = [random_string(len(target)) for _ in range(100)]

    for generation in range(100):
        population = sorted(population, key=fitness, reverse=True)
        if fitness(population[0]) == len(target):
            print(f"Matched in generation {generation}: {population[0]}")
            return

        new_population = []
        while len(new_population) < len(population):
            p1, p2 = select(population)
            child = mutate(crossover(p1, p2))
            new_population.append(child)

        population = new_population

    print(f"Stopped after 100 generations. Best match: {population[0]}")

target = input("Enter the target string: ").lower()
genetic_algorithm(target)