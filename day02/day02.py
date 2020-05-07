
class IntCode:
    def __init__(self, filename: str):
        with open(filename) as f:
            self.mem = [int(i) for i in f.readline().split(',')]
        self.cur = 0

    def process(self):
        while(True):
            op = self[self.cur]
            args = self[self.cur+1:self.cur+4]
            self.cur += 4
            if op == 1:
                self.add(*args)
            elif op == 2:
                self.multiply(*args)
            elif op == 99:
                return

    def add(self, arg1, arg2, ret):
        self[ret] = self[arg1] + self[arg2]

    def multiply(self, arg1, arg2, ret):
        self[ret] = self[arg1] * self[arg2]

    def __getitem__(self, key: int) -> int:
        return self.mem[key]

    def __setitem__(self, key: int, value: int):
        self.mem[key] = value