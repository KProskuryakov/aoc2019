from functools import reduce
from operator import add


def calc_fuel(module_mass: int):
    return module_mass // 3 - 2


def read_input(filename: str):
    with open(filename) as f:
        return [int(line) for line in f.readlines()]


def combined_fuel(filename: str):
    masses = read_input(filename)
    fuels = map(calc_fuel, masses)
    return reduce(add, fuels)


def recur_fuel(module_mass: int):
    total = cur = calc_fuel(module_mass)
    while True:
        cur = calc_fuel(cur)
        if cur > 0:
            total += cur
        else:
            return total


def combined_fuel2(filename: str):
    masses = read_input(filename)
    fuels = map(recur_fuel, masses)
    return reduce(add, fuels)
