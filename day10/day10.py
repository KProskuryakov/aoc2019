from math import gcd


class Slope:
    def __init__(self, p1, p2):
        x = p1[0] - p2[0]
        y = p1[1] - p2[1]
        if x == 0:
            self.x = 0
            self.y = y / abs(y)
        elif y == 0:
            self.x = x / abs(x)
            self.y = 0
        else:
            d = gcd(x, y)
            self.x = x / d
            self.y = y / d

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        if self.x == 0 or self.y == 0:
            return 0
        else:
            return int(10000 * self.x / self.y)


with open("day10/input.txt") as f:
    # Yeah, it's transposed but that doesn't matter
    asteroids = [(i, j) for i, l in enumerate(f) for j, c in enumerate(l) if c == "#"]
    lens = [len(set([Slope(a, b) for b in asteroids if a != b])) for a in asteroids]

    print(lens)
    print(max(lens))
