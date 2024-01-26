# Analyzing RWS and SUS in Genetic Algorithms

This project performs an empirical analysis of the performance of [Roulette Wheel Selection](https://en.wikipedia.org/wiki/Fitness_proportionate_selection) (RWS) and [Stochastic Universal Sampling](https://en.wikipedia.org/wiki/Stochastic_universal_sampling) (SUS), as well as their modifications (with fitness function scaling): disruptive, blended selection, and window selection.

To do this, 100 different populations of size 100 are generated. They are then used in a genetic algorithm that runs until it converges (or reaches 10000 iterations) with every possible combination of the following configurations:
- Binary or Gray encoding;
- 7 different [fitness functions](https://en.wikipedia.org/wiki/Fitness_function);
- 8 different selection methods (as described above);
- [Genetic operators](https://en.wikipedia.org/wiki/Genetic_operator): none/crossover/mutation/both.

The results of the experiments are saved in .xlsx files in addition to graphs that analyze first 5 runs of each experiment in more detail.

## *How to run*

- [Install pip](https://pip.pypa.io/en/stable/installation)
- Install library dependencies: `pip install numpy matplotlib xlsxwriter`
- Edit run configuration in [config.py](config.py) and [main.py](main.py)
- Run `python main.py`