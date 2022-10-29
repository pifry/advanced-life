from turtle import pos
import numpy as np
from itertools import product

# rng = np.random.default_rng(12345)
# world = rng.choice([False, True], CANVAS_SIZE)
RNG = np.random.default_rng(12345)

class Engine:
    @classmethod
    def random(cls, size):
        return cls(size, random=True)

    def __init__(self, size, random=False, default=0) -> None:
        if random:         
            self.data = RNG.choice([0, 1], size)
        else:
            self.data = np.ndarray(size)
            self.data.fill(default)

        self.epoch_no = 0

        self.die_population = list(range(0,7)) + list(range(15,27)) 
        self.born_population = [11,12]

        # Classical Conway's Game of Life Rules
        # self.die_population = list(range(0,2)) + list(range(4,9)) 
        # self.born_population = [3]

    def epoch(self):
        new_data = np.ndarray(self.data.shape)

        ranges = [range(dim) for dim in self.data.shape]

        activity = 0
        size = 0

        for position in product(*ranges):
            nbhd = self.data
            for dim in range(self.data.ndim):
                nbhd = nbhd.take(indices=range(position[dim]-1, position[dim]+1+1), axis=dim, mode='wrap')

            population = np.sum(nbhd) - self.data[position]

            new_data[position] = self.data[position]
            if population in self.die_population:
                new_data[position] = 0
            if population in self.born_population:
                new_data[position] = 1

            if new_data[position] != self.data[position]:
                activity = activity + 1
            if new_data[position] == 1:
                size = size + 1
            
        self.data = new_data
        print(f'epoch {self.epoch_no}: activity: {activity}, size: {size}')
        self.epoch_no = self.epoch_no + 1
