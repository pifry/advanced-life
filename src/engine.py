import numpy as np

# rng = np.random.default_rng(12345)
# world = rng.choice([False, True], CANVAS_SIZE)
RNG = np.random.default_rng(12345)

class Engine:
    @classmethod
    def random(cls, size):
        return cls(size, random=True)

    def __init__(self, size, random=False, default=False) -> None:
        if random:         
            self.data = RNG.choice([False, True], size)
        else:
            self.data = np.ndarray(size)
            self.data.fill(default)