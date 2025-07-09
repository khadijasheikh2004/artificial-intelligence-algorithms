import random
import string

def generate_random_function(length):
    char = ['+', '-', '*', '/', 'x','y','^','z'] + list('0123456789')
    return ''.join(random.choice(char) for _ in range(length))

def create_population(pop_size,target_length):
    return [generate_random_function(target_length) for _ in range(pop_size)]

def calculate_fitness(individual, target):
    """Calculate fitness based on matching characters"""
    return sum(1 for a, b in zip(individual, target) if a == b)

def select_parent(population,fitness_scores):
    tournament_size=3
    list1 = list(enumerate(population))
    tournament = random.sample(range(len(population)),tournament_size)
    best_index = max(tournament, key=lambda idx: fitness_scores[idx])
    return population[best_index]

def crossover(parent1,parent2):
    crossover_point = random.randint(0,len(parent1))
    return parent1[:crossover_point] + parent2[crossover_point:]

def mutate(individual,mutation_rate=0.1):
    individual_list = list(individual)
    char = ['+', '-', '*', '/', 'x','y','^','z'] + list('0123456789')
    for i in range(len(individual_list)):
        if random.random() < mutation_rate:
            individual_list[i]=random.choice(char)
    return ''.join(individual_list)

def genetic_algorithm():
    target = input("Enter a target function: ")
    pop_size =100
    generations = 100
    population = create_population(pop_size,len(target))

    for generation in range(generations):
        fitness_scores = [calculate_fitness(ind,target) for ind in population]
        best_fitness = max(fitness_scores)
        best_individual = population[fitness_scores.index(best_fitness)]

        if best_fitness == len(target):
            print(f"\nSolution found in generation {generation}!")
            print(f"Solution: {best_individual}")
            return
        new_population = []
        for _ in range(pop_size):
            parent1 = select_parent(population,fitness_scores)
            parent2 = select_parent(population,fitness_scores)
            child = crossover(parent1,parent2)
            child= mutate(child)
            new_population.append(child)
        population = new_population
        print(f"Generation {generation}: Best = {best_individual}, Fitness = {best_fitness}")

    print("\nTarget function not found!")

if __name__ == '__main__':
    genetic_algorithm()
    



    