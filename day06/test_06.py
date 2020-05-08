from day06 import create_tree


def test_dummy():
    tree = create_tree("day06/testinput06.txt")
    assert tree.count_orbits() == 42


def test_first_part():
    tree = create_tree("day06/input06.txt")
    assert tree.count_orbits() == 254447


def test_dummy_two():
    tree = create_tree("day06/testinput06_2.txt")
    assert tree.get_path_to("YOU", "SAN") == 4


def test_second_part():
    tree = create_tree("day06/input06.txt")
    assert tree.get_path_to("YOU", "SAN") == 445
