
import time
import random
from DominatingSet import minimalDominatingSet


def randomGraph(n, m):
    vertices = [ "v{}".format(i) for i in range(n) ]
    edges = []

    for _ in range(m):
        while True:
            v1 = vertices[random.randint(0, n-1)]
            v2 = vertices[random.randint(0, n-1)]

            if (v1, v2) not in edges and (v2, v1) not in edges:
                edges.append((v1, v2))
                break

    return (vertices, edges)


def benchmark_minimalDominatingSet():
    for n in [10, 20, 30, 40, 50]:
        for m in range(0, 2*n, n//10):
            vertices, edges = randomGraph(n, m)

            print("n = {}, m = {}...".format(n, m))

            t0 = time.time()
            minimalDominatingSet(vertices, edges)
            dt = time.time() - t0

            print("n = {}, m = {}: {}".format(n, m, dt))


if __name__ == "__main__":
    benchmark_minimalDominatingSet()