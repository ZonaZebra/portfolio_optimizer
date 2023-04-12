from app.ga_solver import initialize_population, evaluate_fitness, selection, crossover, mutation
from app.portfolio import Portfolio
import numpy as np

def test_initialize_population():
    pop_size = 10
    num_assets = 5
    population = initialize_population(pop_size, num_assets)

    assert len(population) == pop_size
    for individual in population:
        assert len(individual) == num_assets
        assert np.isclose(np.sum(individual), 1)

def test_evaluate_fitness():
    weights = np.array([0.4, 0.6])
    returns = np.array([[0.01, 0.02], [0.02, 0.03], [0.03, 0.04]])
    risk_free_rate = 0.02
    fitness = evaluate_fitness(weights, returns, risk_free_rate)
    portfolio = Portfolio(weights, returns)
    expected_fitness = portfolio.sharpe_ratio(risk_free_rate)
    assert np.isclose(fitness, expected_fitness)

def test_selection():
    population = [np.array([0.4, 0.6]), np.array([0.3, 0.7]), np.array([0.5, 0.5])]
    fitness_scores = [1.0, 1.5, 0.5]
    selection_size = 2
    selected = selection(population, fitness_scores, selection_size)

    assert len(selected) == selection_size
    assert (np.array_equal(selected[0], population[1]) and np.array_equal(selected[1], population[0])) or \
           (np.array_equal(selected[0], population[0]) and np.array_equal(selected[1], population[1]))


def test_crossover():
    parent1 = np.array([0.4, 0.6])
    parent2 = np.array([0.3, 0.7])
    child1, child2 = crossover(parent1, parent2)

    assert len(child1) == len(parent1)
    assert len(child2) == len(parent2)
    assert np.isclose(np.sum(child1), 1)
    assert np.isclose(np.sum(child2), 1)

def test_mutation():
    individual = np.array([0.4, 0.6])
    mutation_rate = 0.1
    mutated = mutation(individual, mutation_rate)

    assert len(mutated) == len(individual)
    assert np.isclose(np.sum(mutated), 1)
