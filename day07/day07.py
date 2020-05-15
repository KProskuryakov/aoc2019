from copy import deepcopy
from itertools import permutations, chain
from asyncio import Queue
import asyncio
from typing import List, Tuple, cast


class IntCode:
    def __init__(self, program_str: str, input_queue: Queue, output_queue: Queue):
        self.mem = [int(i) for i in program_str.split(",")]
        self.cur = 0
        self.input_queue: Queue = input_queue
        self.output_queue: Queue = output_queue

    async def process(self):
        outputs = []
        while True:
            op = self.cur_op()
            if op == 1:
                self.add()
            elif op == 2:
                self.multiply()
            elif op == 3:
                await self.input()
            elif op == 4:
                self.output()
            elif op == 5:
                self.jump_if_true()
            elif op == 6:
                self.jump_if_false()
            elif op == 7:
                self.less_than()
            elif op == 8:
                self.equals()
            elif op == 99:
                return
            else:
                raise Exception(f"Op {op} is not valid.")

    def add(self):
        arg1 = self.arg_get(1)
        arg2 = self.arg_get(2)
        self.arg_set(3, arg1 + arg2)
        self.cur += 4

    def multiply(self):
        arg1 = self.arg_get(1)
        arg2 = self.arg_get(2)
        self.arg_set(3, arg1 * arg2)
        self.cur += 4

    async def input(self):
        val = await self.input_queue.get()
        self.arg_set(1, val)
        self.cur += 2

    def output(self):
        self.output_queue.put_nowait(self.arg_get(1))
        self.cur += 2

    def jump_if_true(self):
        arg1 = self.arg_get(1)
        arg2 = self.arg_get(2)
        if arg1 != 0:
            self.cur = arg2
        else:
            self.cur += 3

    def jump_if_false(self):
        arg1 = self.arg_get(1)
        arg2 = self.arg_get(2)
        if arg1 == 0:
            self.cur = arg2
        else:
            self.cur += 3

    def less_than(self):
        arg1 = self.arg_get(1)
        arg2 = self.arg_get(2)
        if arg1 < arg2:
            self.arg_set(3, 1)
        else:
            self.arg_set(3, 0)
        self.cur += 4

    def equals(self):
        arg1 = self.arg_get(1)
        arg2 = self.arg_get(2)
        if arg1 == arg2:
            self.arg_set(3, 1)
        else:
            self.arg_set(3, 0)
        self.cur += 4

    def arg_get(self, pos):
        op_str = self.cur_op_str()
        mode = int(op_str[-2 - pos])
        immediate = self[self.cur + pos]
        if mode == 0:  # Position mode
            return self[immediate]
        elif mode == 1:  # Immediate mode
            return immediate

    def arg_set(self, pos, val):
        write_loc = self[self.cur + pos]
        self[write_loc] = val

    def cur_op(self):
        op_str = self.cur_op_str()
        return int(op_str[-2:])

    def cur_op_str(self):
        return format(self[self.cur], "05d")

    def __getitem__(self, key: int) -> int:
        return self.mem[key]

    def __setitem__(self, key: int, value: int):
        self.mem[key] = value


async def pipe_process(program_str: str, phase_range) -> int:
    perms = cast(List[Tuple[int]], list(permutations(phase_range, 5)))

    max_list = await asyncio.gather(
        *(compute_perm(program_str, perm) for perm in perms)
    )

    return max(max_list)


async def compute_perm(program_str, perm: Tuple[int]):
    queues: List[Queue] = [Queue() for _ in range(5)]
    one_off_queues = chain(queues[1:], queues[0:1])
    queue_pairs = list(zip(queues, one_off_queues))
    programs = [IntCode(program_str, iq, oq) for iq, oq in queue_pairs]

    for q, p in zip(queues, perm):
        q.put_nowait(p)

    queues[0].put_nowait(0)

    await asyncio.gather(*(prg.process() for prg in programs))

    return (queues[0].get_nowait(), perm)
