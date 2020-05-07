from day03 import Wire, manhattan, fewest_steps


def test_make_wire():
    wire = Wire("R8,U5,L5,D3")
    assert wire.vecs == [("R", 8), ("U", 5), ("L", 5), ("D", 3)]


def test_iter():
    wire = Wire("R3,U1,L2,D4")
    assert list(wire) == [
        (1, 0),
        (2, 0),
        (3, 0),
        (3, 1),
        (2, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (1, -2),
        (1, -3),
    ]


def test_intersect():
    wire1 = Wire("R8,U5,L5,D3")
    wire2 = Wire("U7,R6,D4,L4")
    assert wire1.intersect(wire2) == {(3, 3), (6, 5)}


def test_manhattan():
    wire1 = Wire("R8,U5,L5,D3")
    wire2 = Wire("U7,R6,D4,L4")
    assert manhattan(wire1, wire2) == 6


def test_first_part():
    with open("day03/input03.txt") as f:
        wire1 = Wire(f.readline())
        wire2 = Wire(f.readline())
        assert manhattan(wire1, wire2) == 1225


def test_second_part():
    with open("day03/input03.txt") as f:
        wire1 = Wire(f.readline())
        wire2 = Wire(f.readline())
        assert fewest_steps(wire1, wire2) == 107036
