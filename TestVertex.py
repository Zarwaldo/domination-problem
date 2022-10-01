
import random
from Graph import Edge, Vertex


def test_getName():
    for name in ["test_name1", "", "VERTEX", "T43ztze"]:
        if Vertex(name).getName() != name:
            return False

    return True


def test_setMarked():
    for bool in [False, True]:
        vertex = Vertex("name")
        vertex.setMarked(bool)

        if vertex.isMarked() != bool:
            return False

    return True


def test_cover():
    for n in range(50):
        center = Vertex("center")

        neighboors = []
        edges = []

        for i in range(n):
            neighboor = Vertex("neighboor {}".format(i))
            neighboors.append(neighboor)

            edge = Edge("edge {}".format(i), center, neighboor)
            edges.append(edge)

        center.cover()

        for i in range(n):
            if not neighboors[i].isMarked():
                return False

    return True


def test_getCoveringPotential():
    for n in range(50):
        center = Vertex("center")

        neighboors = []
        edges = []

        r = random.randint(0, n)

        for i in range(n):
            neighboor = Vertex("neighboor {}".format(i))
            neighboors.append(neighboor)

            edge = Edge("edge {}".format(i), center, neighboor)
            edges.append(edge)

        for i in range(r):
            neighboors[i].setMarked()

        if center.getCoveringPotential() != n - r + 1:
            return False

    return True


if __name__ == "__main__":
    if not test_getName():
        print("ERROR on getName")

    if not test_setMarked():
        print("ERROR on setMarked")

    if not test_cover():
        print("ERROR on cover")

    if not test_getCoveringPotential():
        print("ERROR on getCoveringPotential")