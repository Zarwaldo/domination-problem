

from Graph import *


def test_buildGraph():
    vertices = ["v1", "v2", "v3", "v4", "v5"]
    edges = [
        ("v1", "v3"),
        ("v1", "v4"),
        ("v1", "v5"),
        ("v2", "v3"),
        ("v2", "v4"),
        ("v2", "v5"),
        ("v3", "v4")
    ]

    graph = buildGraph(vertices, edges)

    if sorted(vertices) != sorted([ v.getName() for v in graph.getVertices() ]):
        return False

    if sorted(edges) != sorted([ (e.vertex1.getName(), e.vertex2.getName()) for e in graph.getEdges() ]):
        return False

    return True


def test_copy():
    vertices = ["v1", "v2", "v3", "v4", "v5"]
    edges = [
        ("v1", "v3"),
        ("v1", "v4"),
        ("v1", "v5"),
        ("v2", "v3"),
        ("v2", "v4"),
        ("v2", "v5"),
        ("v3", "v4")
    ]

    graph = buildGraph(vertices, edges)
    graph_ = graph.copy()

    if sorted(vertices) != sorted([ v.getName() for v in graph_.getVertices() ]):
        return False

    if sorted(edges) != sorted([ (e.vertex1.getName(), e.vertex2.getName()) for e in graph_.getEdges() ]):
        return False

    return True


def test_getConnectedComponents():
    test_base = [
        {
            "vertices": [],
            "edges": []
        },
        {
            "vertices": ["v1", "v2", "v3", "v4", "v5"],
            "edges": [
                ("v1", "v2"),
                ("v2", "v3"),
                ("v4", "v5")
            ]
        },
        {
            "vertices": ["v1", "v2", "v3", "v4", "v5"],
            "edges": [
                ("v1", "v2"),
                ("v1", "v3"),
                ("v2", "v3"),
                ("v4", "v5")
            ]
        },
        {
            "vertices": ["v1", "v2", "v3", "v4", "v5"],
            "edges": [
                ("v1", "v2"),
                ("v1", "v3"),
                ("v2", "v3"),
                ("v3", "v4")
            ]
        },
        {
            "vertices": ["v1", "v2", "v3", "v4", "v5"],
            "edges": []
        }
    ]

    for test in test_base:
        graph = buildGraph(test["vertices"], test["edges"])
        print([ v.getName() for v in graph.getVertices() ], [ e.getName() for e in graph.getEdges() ])
        components : List[Graph] = graph.getConnectedComponents()
        for component in components:
            print('-', [ v.getName() for v in component.getVertices() ], [ e.getName() for e in component.getEdges() ])

    return True


def test_getUnmarkedConnectedComponents():
    graph = buildGraph(
        ["v1", "v2", "v3", "v4", "v5", "v6", "v7", "v8", "v9", "v10", "v11", "v12", "v13", "v14", "v15"],
        [
            ("v1", "v2"),
            ("v1", "v6"),
            ("v2", "v3"),
            ("v2", "v7"),
            ("v3", "v4"),
            ("v3", "v8"),
            ("v4", "v5"),
            ("v4", "v9"),
            ("v6", "v2"),
            ("v6", "v7"),
            ("v6", "v10"),
            ("v7", "v3"),
            ("v7", "v8"),
            ("v7", "v11"),
            ("v8", "v4"),
            ("v8", "v9"),
            ("v8", "v12"),
            ("v9", "v5"),
            ("v10", "v7"),
            ("v10", "v11"),
            ("v10", "v13"),
            ("v11", "v8"),
            ("v11", "v12"),
            ("v11", "v14"),
            ("v12", "v9"),
            ("v13", "v11"),
            ("v13", "v14"),
            ("v13", "v15"),
            ("v14", "v12"),
            ("v15", "v14")
        ]
    )

    graph.getVertexByName("v3").setMarked()
    graph.getVertexByName("v7").setMarked()
    graph.getVertexByName("v8").setMarked()
    graph.getVertexByName("v10").setMarked()
    graph.getVertexByName("v11").setMarked()
    graph.getVertexByName("v12").setMarked()
    graph.getVertexByName("v13").setMarked()
    graph.getVertexByName("v14").setMarked()

    print([ v.getName() for v in graph.getVertices() ], [ e.getName() for e in graph.getEdges() ])

    components : List[Graph] = graph.getUnmarkedConnectedComponents()
    for component in components:
        print('-', [ v.getName() for v in component.getVertices() ], [ e.getName() for e in component.getEdges() ])

    return True


def test_getDisk():
    graph = buildGraph(["v1", "v2", "v3", "v4"], [("v1", "v2"), ("v2", "v3"), ("v3", "v4")])

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v1") ], 0) ]) != sorted([ "v1" ]):
        return False

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v1") ], 1) ]) != sorted([ "v1", "v2" ]):
        return False

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v1") ], 2) ]) != sorted([ "v1", "v2", "v3" ]):
        return False

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v1") ], 3) ]) != sorted([ "v1", "v2", "v3", "v4" ]):
        return False

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v2") ], 0) ]) != sorted([ "v2" ]):
        return False

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v2") ], 1) ]) != sorted([ "v1", "v2", "v3" ]):
        return False

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v2") ], 2) ]) != sorted([ "v1", "v2", "v3", "v4" ]):
        return False


    graph = buildGraph(
        ["v0", "v1", "v2", "v3", "v4", "v5", "v11", "v22", "v33", "v44", "v55"],
        [
            ("v0", "v1"),
            ("v0", "v2"),
            ("v0", "v3"),
            ("v0", "v4"),
            ("v0", "v5"),
            ("v5", "v1"),
            ("v1", "v2"),
            ("v2", "v3"),
            ("v3", "v4"),
            ("v4", "v5"),
            ("v1", "v11"),
            ("v2", "v22"),
            ("v3", "v33"),
            ("v4", "v44"),
            ("v5", "v55")
        ]
    )


    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v0") ], 0) ]) != sorted([ "v0" ]):
        return False

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v0") ], 1) ]) != sorted([ "v0", "v1", "v2", "v3", "v4", "v5" ]):
        return False

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v0") ], 2) ]) != sorted([ "v0", "v1", "v2", "v3", "v4", "v5", "v11", "v22", "v33", "v44", "v55" ]):
        return False

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v11") ], 0) ]) != sorted([ "v11" ]):
        return False

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v11") ], 1) ]) != sorted([ "v11", "v1" ]):
        return False

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v11") ], 2) ]) != sorted([ "v11", "v1", "v2", "v5", "v0" ]):
        return False

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v11") ], 3) ]) != sorted([ "v11", "v1", "v2", "v0", "v5", "v22", "v3", "v4", "v55" ]):
        return False

    if sorted([ v.getName() for v in graph.getDisk([ graph.getVertexByName("v11") ], 4) ]) != sorted([ "v11", "v1", "v2", "v0", "v5", "v22", "v3", "v4", "v55", "v33", "v44" ]):
        return False

    return True


if __name__ == "__main__":
    if not test_buildGraph():
        print("ERROR in buildGraph")
    if not test_copy():
        print("ERROR in copy")
    if not test_getConnectedComponents():
        print("ERROR in getConnectedComponents")
    if not test_getUnmarkedConnectedComponents():
        print("ERROR in getUnmarkedConnectedComponents")
    if not test_getDisk():
        print("ERROR in getDisk")