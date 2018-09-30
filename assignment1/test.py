import hw1
import numpy as np

#Testing methods
print(hw1.histogram_times("airplane_crashes.csv"))
print(hw1.weigh_pokemons("pokedex.json", 10.0))
print(hw1.single_type_candy_count("pokedex.json"))
print(hw1.reflections_and_projections(np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])))
print(hw1.normalize(np.array([[0, 5, 3], [255, 146, 26], [12, 56, 79]])))
print(hw1.sigmoid_normalize(np.array([[1, 199], [3, 255]]), 25))
