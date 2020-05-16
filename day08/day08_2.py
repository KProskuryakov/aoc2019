from itertools import islice, groupby

with open("day08/input08.txt") as f:
    img = f.read()
    w = 25
    h = 6

    img_iter = iter(img)

    layers = [list(islice(img_iter, w * h)) for _ in range(len(img) // w // h)]

    top_layer = layers[0]

    for layer in layers:
        for idx, num in enumerate(layer):
            if top_layer[idx] == "2":
                top_layer[idx] = num

    for y in range(h):
        dummy = [top_layer[y * w + x] for x in range(w)]
        print("".join(dummy).replace("0", " "))
