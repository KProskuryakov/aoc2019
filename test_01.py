from day01 import calc_fuel, read_input, combined_fuel, recur_fuel, combined_fuel2


def test_calc_fuel():
    assert calc_fuel(12) == 2
    assert calc_fuel(14) == 2
    assert calc_fuel(1969) == 654
    assert calc_fuel(100756) == 33583


def test_combined_fuel():
    assert combined_fuel("input01.txt") == 3515171


def test_recur_fuel():
    assert recur_fuel(14) == 2
    assert recur_fuel(1969) == 966
    assert recur_fuel(100756) == 50346


def test_combined_fuel2():
    assert combined_fuel2("input01.txt") == 5269882
