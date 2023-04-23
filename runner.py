from stats.experiment_stats import ExperimentStats
from evo_algorithm import EvoAlgorithm
from model.population import Population
from selection.selection_method import SelectionMethod
from model.gen_operators import GeneticOperator
from copy import deepcopy
from datetime import datetime

def run_experiment(selection_method: SelectionMethod,
                   genetic_operator: GeneticOperator,
                   param_names: tuple[str],
                   populations: list[Population]):
    stats = ExperimentStats(param_names)

    for (run_i, population) in enumerate(populations):
        init_population = deepcopy(population)
        selection_method.initialize()
        
        current_run = EvoAlgorithm(init_population, selection_method, genetic_operator, param_names).run(run_i)
        stats.add_run(current_run)

    stats.calculate()

    print(f'{str(datetime.now())[:-4]} | Experiment ({"|".join(param_names)}) finished')
    
    return stats
