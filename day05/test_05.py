from day05 import IntCode


def test_first_part():
    program = IntCode("day05/input05.txt")
    outputs = program.process([1])

    assert outputs[-1] == 11933517


def test_second_part():
    program = IntCode("day05/input05.txt")
    outputs = program.process([5])

    assert outputs[-1] == 10428568
