import numpy as np


def generate_uniform_int(rng, n):
    return rng.integers(20, 41, size=n)


def generate_uniform_real(rng, n):
    return rng.uniform(2.0, 3.0, size=n)


def generate_normal(rng, n):
    return rng.normal(0, 0.5, size=n)


def generate_exponential(rng, n):
    return rng.exponential(4, size=n)


def generate_poisson(rng, n):
    return rng.poisson(5, size=n)


DISTRIBUTIONS = {
    "Uniform (int)": {
        "generator": generate_uniform_int,
        "theo_mean": 30.0,
        "theo_std": 6.06,
        "discrete": True,
        "pdf": None,
    },
    "Uniform (real)": {
        "generator": generate_uniform_real,
        "theo_mean": 2.5,
        "theo_std": 0.289,
        "discrete": False,
        "pdf": None,
    },
    "Normal": {
        "generator": generate_normal,
        "theo_mean": 0.0,
        "theo_std": 0.5,
        "discrete": False,
        "pdf": None,
    },
    "Exponential": {
        "generator": generate_exponential,
        "theo_mean": 4.0,
        "theo_std": 4.0,
        "discrete": False,
        "pdf": None,
    },
    "Poisson": {
        "generator": generate_poisson,
        "theo_mean": 5.0,
        "theo_std": 2.236,
        "discrete": True,
        "pdf": None,
    },
}
