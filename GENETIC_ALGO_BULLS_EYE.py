
'''

Author: Anuj Suresh Sonawane
Project: Hitting bull's eye using genetic algorithm

'''

import pygame
import random

# Constants
WIDTH = 800
HEIGHT = 600
TARGET_RADIUS = 20
POPULATION_SIZE = 100
GENOME_LENGTH = 300
MUTATION_RATE = 0.01
DRAWN_INDIVIDUALS = 10  # Number of individuals to draw in the visualization

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def evaluate_fitness(genome):
    x = WIDTH // 2
    y = HEIGHT // 2
    vx = 0
    vy = 0
    for gene in genome:
        vx += gene[0]
        vy += gene[1]
        x += vx
        y += vy
        if x < TARGET_RADIUS or x > WIDTH - TARGET_RADIUS or y < TARGET_RADIUS or y > HEIGHT - TARGET_RADIUS:
            break
    distance = calculate_distance(x, y, WIDTH // 2, HEIGHT // 2)
    fitness = 1 / (distance + 1)
    return fitness, (x, y)

def create_population():
    population = []
    for _ in range(POPULATION_SIZE):
        genome = []
        for _ in range(GENOME_LENGTH):
            gene = (random.uniform(-1, 1), random.uniform(-1, 1))
            genome.append(gene)
        population.append(genome)
    return population

def select_parents(population):
    fitness_sum = sum([evaluate_fitness(genome)[0] for genome in population])
    probabilities = [evaluate_fitness(genome)[0] / fitness_sum for genome in population]
    parents = random.choices(population, weights=probabilities, k=2)
    return parents

def crossover(parent1, parent2):
    point = random.randint(1, GENOME_LENGTH - 1)
    offspring1 = parent1[:point] + parent2[point:]
    offspring2 = parent2[:point] + parent1[point:]
    return offspring1, offspring2

def mutate(genome):
    for i in range(len(genome)):
        if random.random() < MUTATION_RATE:
            genome[i] = (random.uniform(-1, 1), random.uniform(-1, 1))
    return genome

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Genetic Algorithm - Bulls Eye")
    clock = pygame.time.Clock()

    population = create_population()

    done = False
    generation = 1
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Evaluate fitness
        fitness_scores = [evaluate_fitness(genome) for genome in population]

        # Find the best genome
        best_fitness, best_position = max(fitness_scores)

        # Create new population
        new_population = [population[0]]  # Preserve the best genome

        # Generate offspring
        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = select_parents(population)
            offspring1, offspring2 = crossover(parent1, parent2)
            offspring1 = mutate(offspring1)
            offspring2 = mutate(offspring2)
            new_population.extend([offspring1, offspring2])

        population = new_population
        generation += 1

        # Draw the population
        screen.fill((0, 0, 0))

        # Draw a subset of individuals
        drawn_individuals = random.sample(population, DRAWN_INDIVIDUALS)
        for genome in drawn_individuals:
            x = WIDTH // 2
            y = HEIGHT // 2
            vx = 0
            vy = 0
            for gene in genome:
                vx += gene[0]
                vy += gene[1]
                x += vx
                y += vy
                pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 2)

        # Draw the target
        pygame.draw.circle(screen, (255, 0, 0), (WIDTH // 2, HEIGHT // 2), TARGET_RADIUS)

        # Draw the best genome
        pygame.draw.circle(screen, (0, 255, 0), (int(best_position[0]), int(best_position[1])), 5)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
