from itertools import accumulate, repeat, takewhile


def calc_fuel(module_mass: int):
    return module_mass // 3 - 2


def read_input(filename: str):
    with open(filename) as f:
        return [int(line) for line in f]


def combined_fuel(filename: str, fuel_func):
    masses = read_input(filename)
    return sum(fuel_func(m) for m in masses)


def calc_fuel2(module_mass: int):
    initial_fuel_mass = calc_fuel(module_mass)
    recursive_fuels = accumulate(repeat(initial_fuel_mass), lambda m, _: calc_fuel(m))
    return sum(takewhile(lambda f: f > 0, recursive_fuels))
