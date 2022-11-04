"""Run experiments comparing various approaches of summing an array of
floating-point values."""

from math import fsum
import numpy as np


def ksum(nums):
    """Sum an iterable of floating-point values using the Kahan summation
    algorithm.

    See the algorithm's description: https://www.wikiwand.com/en/Kahan_summation_algorithm
    """

    s = 0.0
    c = 0.0

    for num in nums:
        y = num - c
        t = s + y
        c = (t - s) - y
        s = t

    return s


def run_experiment(n: int):
    nums = np.random.randn(n)

    print(f"n = {n}")
    print(f"sum(nums): \t{sum(nums):20.15f}")
    print(f"fsum(nums):\t{fsum(nums):20.15f}")
    print(f"ksum(nums):\t{ksum(nums):20.15f}")
    print()


ns = [10, 50, 500, 1_000, 10_000, 100_000, 1_000_000]
for n in ns:
    run_experiment(n)
