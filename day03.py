d = {
    "R": lambda x, y: (x + 1, y),
    "L": lambda x, y: (x - 1, y),
    "U": lambda x, y: (x, y + 1),
    "D": lambda x, y: (x, y - 1),
}


class Wire:
    def __init__(self, path: str):
        self.vecs = [(v[0], int(v[1:])) for v in path.split(",")]

    def __iter__(self):
        x, y = 0, 0
        for vd, vm in self.vecs:
            for _ in range(vm):
                x, y = d[vd](x, y)
                yield (x, y)

    def intersect(self, wire: "Wire"):
        return set(self).intersection(set(wire))

    def steps_to(self, loc):
        for i, cur in enumerate(self):
            if cur == loc:
                return i + 1


def manhattan(wire1: Wire, wire2: Wire):
    crosses = wire1.intersect(wire2)
    dists = [abs(x) + abs(y) for x, y in crosses]
    return min(dists)


def fewest_steps(wire1: Wire, wire2: Wire):
    crosses = wire1.intersect(wire2)
    dists = [wire1.steps_to(loc) + wire2.steps_to(loc) for loc in crosses]
    return min(dists)
