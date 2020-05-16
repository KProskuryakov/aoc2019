from itertools import islice, groupby

with open("day08/input08.txt") as f:
    img = f.read()
    w = 25
    h = 6

    img_iter = iter(img)

    layers = [list(islice(img_iter, w * h)) for _ in range(len(img) // w // h)]

    grouped_layers = [groupby(sorted(layer)) for layer in layers]

    counts = [[sum(1 for _ in v) for k, v in g] for g in grouped_layers]

    smallest = min(counts)

    print(smallest)

    print(smallest[1] * smallest[2])
