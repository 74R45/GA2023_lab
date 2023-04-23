from main import generate_all_populations_for_fitness_function
from model.encoding import *
from model.fitness_functions import *
from selection.sus import *
from selection.rws import *
from model.gen_operators import *
import time
from evo_algorithm import EvoAlgorithm
import multiprocessing

if __name__ == '__main__': 
    # ff = FconstALL(100)
    # pop = ff.generate_population_for_run(0)
    # start = time.time()
    # EvoAlgorithm(
    #     pop,
    #     DisruptiveRWS(), CrossoverAndMutation, ('FconstALL', 'SUS', 'no_gen_op')).run(0)
    # end = time.time()
    # print(f'Total: {(end - start):.2f}s.')
    print(multiprocessing.cpu_count())