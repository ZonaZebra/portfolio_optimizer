import random
import numpy as np
from dask import delayed, compute
from dask.distributed import Client
from app.portfolio import Portfolio

def initialize_population(pop_size, num_assets):
    population = []
    for _ in range(pop_size):
        individual = np.random.dirichlet(np.ones(num_assets))
        population.append(individual)
    return population

def evaluate_fitness(individual, returns, risk_free_rate):
    portfolio = Portfolio(individual, returns)
    sharpe_ratio = portfolio.sharpe_ratio(risk_free_rate)
    return sharpe_ratio

def selection(population, fitness_scores, selection_size):
    selected_indices = np.argsort(fitness_scores)[-selection_size:]
    return [population[i] for i in selected_indices]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))

    # Normalize the children's weights
    child1 /= np.sum(child1)
    child2 /= np.sum(child2)

    return child1, child2


def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            mutation_amount = random.uniform(-0.1, 0.1)
            individual[i] += mutation_amount
            individual = np.clip(individual, 0, 1)
            individual /= np.sum(individual)
    return individual

def ga_solver(returns, pop_size, num_generations, risk_free_rate=0.02):
    num_assets = returns.shape[1]
    population = initialize_population(pop_size, num_assets)

    for generation in range(num_generations):
        # Calculate fitness scores for the current population
        fitness_scores = [delayed(evaluate_fitness)(ind, returns, risk_free_rate) for ind in population]
        fitness_scores = compute(*fitness_scores)

        # Select the best individuals
        selected_individuals = selection(population, fitness_scores, pop_size // 2)

        # Create the next generation through crossover and mutation
        next_gen = []
        for _ in range(pop_size // 2):
            parent1 = random.choice(selected_individuals)
            parent2 = random.choice(selected_individuals)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutation(child1, 0.1)
            child2 = mutation(child2, 0.1)
            next_gen.extend([child1, child2])

        population = next_gen

    best_fitness_index = np.argmax(fitness_scores)
    best_individual = population[best_fitness_index]
    best_fitness = fitness_scores[best_fitness_index]

    return best_individual, best_fitness

