import logging


class IntCode:
    def __init__(self, filename: str):
        with open(filename) as f:
            self.mem = [int(i) for i in f.readline().split(",")]
        self.cur = 0

    def process(self, inputs):
        outputs = []
        while True:
            op = self.cur_op()
            if op == 1:
                self.add()
            elif op == 2:
                self.multiply()
            elif op == 3:
                self.input(inputs)
            elif op == 4:
                self.output(outputs)
            elif op == 5:
                self.jump_if_true()
            elif op == 6:
                self.jump_if_false()
            elif op == 7:
                self.less_than()
            elif op == 8:
                self.equals()
            elif op == 99:
                return outputs
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

    def input(self, inputs):
        self.arg_set(1, inputs.pop(0))
        self.cur += 2

    def output(self, outputs):
        outputs.append(self.arg_get(1))
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
