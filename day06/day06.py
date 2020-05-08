from typing import Dict


class CelestialMass:
    def __init__(self, name):
        self.name = name
        self.orbits = set()
        self.parent = None

    def count_links_to_root(self):
        cur = self
        depth = 0
        while cur.parent != None:
            depth += 1
            cur = cur.parent
        return depth

    def get_path_to_root(self):
        cur = self
        path = set()
        while cur.parent != None:
            path.add(cur.name)
            cur = cur.parent
        return path


class PlanetMap:
    def __init__(self, orbit_strs):
        self.table: Dict[str, CelestialMass] = dict()
        for orbit in orbit_strs:
            parent_str, child_str = orbit.split(")")
            parent_node = self.table.setdefault(parent_str, CelestialMass(parent_str))
            child_node = self.table.setdefault(child_str, CelestialMass(child_str))
            child_node.parent = parent_node
            parent_node.orbits.add(child_node)

    def count_orbits(self):
        return sum(node.count_links_to_root() for node in self.table.values())

    def get_path_to(self, begin, end):
        node1 = self.table[begin]
        node2 = self.table[end]
        path1 = node1.get_path_to_root()
        path2 = node2.get_path_to_root()
        xor = path1 ^ path2
        return len(xor) - 2


def create_tree(filename):
    with open(filename) as f:
        orbit_strs = f.read().splitlines()
        return PlanetMap(orbit_strs)
