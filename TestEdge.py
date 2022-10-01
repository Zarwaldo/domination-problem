
from Graph import Vertex, Edge


def test_getName():
    v1 = Vertex("v1")
    v2 = Vertex("v2")
    for name in ["test_name1", "", "VERTEX", "T43ztze"]:
        if Edge(name, v1, v2).getName() != name:
            return False

    return True


def test_opposite():
    v1 = Vertex("v1")
    v2 = Vertex("v2")
    edge = Edge("edge", v1, v2)

    if edge.opposite(v1) != v2:
        return False

    if edge.opposite(v2) != v1:
        return False

    return True


if __name__ == "__main__":
    if not test_getName():
        print("ERROR in test_getName")

    if not test_opposite():
        print("ERROR in test_opposite")