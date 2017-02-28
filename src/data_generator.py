import numpy as np


class DataGenerator(object):
    @staticmethod
    def linear(relationship, x_min, x_max,
               sample_size=100, noise_mean=0, noise_var=1, seed=1024):
        x = np.linspace(x_min, x_max, sample_size)
        y = np.zeros(sample_size)
        for i in range(sample_size):
            y[i] = relationship(x[i]) + np.random.normal(noise_mean, noise_var)
        return x, y
