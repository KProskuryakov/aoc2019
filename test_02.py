from day02 import IntCode
from copy import deepcopy


def test_first_part():
    program = IntCode("input02.txt")
    program[1] = 12
    program[2] = 2
    program.process()

    assert program.mem[0] == 5482655


def test_second_part():
    program = IntCode("input02.txt")
    for i in range(0, 100):
        for j in range(0, 100):
            cur = deepcopy(program)
            cur[1] = i
            cur[2] = j
            cur.process()
            print(cur[0])
            if cur[0] == 19690720:
                assert i * 100 + j == 4967
                return
    raise Exception("Failed")
