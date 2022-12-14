
from typing import List, Tuple, Optional

class Edge():
    pass


class Vertex():

    def __init__(self, name : str):
        self.name : str = name
        self.mark : bool = False
        self.neighboor_edges : List[Edge] = []


    def getName(self):
        return self.name


    def addEdge(self, edge : Edge):
        self.neighboor_edges.append(edge)


    def setMarked(self, bool : bool = True) -> bool:
        modified = (self.mark != bool)
        self.mark = bool
        return modified


    def isMarked(self) -> bool:
        return self.mark


    def cover(self):
        modif = []

        if self.setMarked():
            modif.append(self)

        for edge in self.neighboor_edges:
            n = edge.opposite(self)
            if n.setMarked():
                modif.append(n)

        return modif


    def getNeighboorVertices(self):
        return [ e.opposite(self) for e in self.neighboor_edges ]


    def getCoveringPotential(self):
        neighboors = [ edge.opposite(self) for edge in self.neighboor_edges ]
        return len([ v for v in [self] + neighboors if not v.isMarked() ])


class Edge():

    def __init__(self, name : str, vertex1 : Vertex, vertex2 : Vertex):
        self.name = name
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex1.addEdge(self)
        self.vertex2.addEdge(self)


    def getName(self):
        return self.name


    def opposite(self, vertex : Vertex) -> Optional[Vertex]:
        if vertex == self.vertex1:
            return self.vertex2

        if vertex == self.vertex2:
            return self.vertex1

        return None


class Graph():

    def __init__(self, vertices : List[Vertex], edges : List[Edge]):
        self.vertices = vertices
        self.edges = edges


    def getVertices(self) -> List[Vertex]:
        return self.vertices


    def getEdges(self) -> List[Edge]:
        return self.edges


    def getVertexByName(self, name : str) -> Vertex:
        return [ v for v in self.getVertices() if v.getName() == name ][0]


    def revert(self, modif : List[Vertex]):
        for v in modif:
            v.setMarked(False)


    def copy(self):
        new_vertices = {}
        for v in self.getVertices():
            v_ = Vertex(v.getName())
            v_.setMarked(v.isMarked())
            new_vertices[v.getName()] = v_

        new_edges = []
        for e in self.getEdges():
            new_edges.append(
                Edge(
                    e.getName(),
                    new_vertices[e.vertex1.getName()],
                    new_vertices[e.vertex2.getName()]
                )
            )

        return Graph([ v for v in new_vertices.values() ], new_edges)


    def topologicalSearch(self, begining : Vertex, neighboorhood, action):
        explored = { v.getName(): False for v in self.getVertices() }

        def explore(v : Vertex):
            explored[v.getName()] = True
            action(v)

            for v_ in neighboorhood(v):
                if not explored[v_.getName()]:
                    explore(v_)

        explore(begining)


    def getSubgraph(self, vertices : List[Vertex]):
        edges = [ e for e in self.getEdges() if e.vertex1 in vertices and e.vertex2 in vertices ]

        new_vertices = {}
        for v in vertices:
            v_ = Vertex(v.getName())
            v_.setMarked(v.isMarked())
            new_vertices[v.getName()] = v_

        new_edges = []
        for e in edges:
            new_edges.append(
                Edge(
                    e.getName(),
                    new_vertices[e.vertex1.getName()],
                    new_vertices[e.vertex2.getName()]
                )
            )

        return Graph([ v for v in new_vertices.values() ], new_edges)


    def getConnectedComponents(self):
        result = []
        components = []
        remaining = [ v.getName() for v in self.getVertices() ]

        def action(v : Vertex):
            if v.getName() in remaining:
                remaining.remove(v.getName())
            components[-1].append(v)

        def neighboorhood(v : Vertex) -> List[Vertex]:
            return v.getNeighboorVertices()

        while len(remaining) > 0:
            components.append([])
            name = remaining[0]
            self.topologicalSearch(self.getVertexByName(name), neighboorhood, action)

        for component in components:
            result.append(self.getSubgraph(component))

        return result


    def getUnmarkedConnectedComponents(self):
        result = []
        components = []
        remaining = [ v.getName() for v in self.getVertices() if not v.isMarked() ]

        def action(v : Vertex):
            if v.getName() in remaining:
                remaining.remove(v.getName())
            components[-1].append(v)

        def neighboorhood(v : Vertex) -> List[Vertex]:
            r = (
                v.getNeighboorVertices()
                if not v.isMarked()
                else [ v_ for v_ in v.getNeighboorVertices() if not v_.isMarked() ]
            )
            return r

        while len(remaining) > 0:
            components.append([])
            name = remaining[0]
            self.topologicalSearch(self.getVertexByName(name), neighboorhood, action)

        for component in components:
            result.append(self.getSubgraph(component))

        return result


    def getDisk(self, centers : List[Vertex], radius : int) -> List[Vertex]:
        if radius <= 0:
            return centers
        
        r = centers.copy()

        for v in self.getDisk(centers, radius - 1):
            for n in v.getNeighboorVertices():
                if n not in r:
                    r.append(n)

        return r



def buildGraph(vertices : List[str], edges : List[Tuple[str]]) -> Graph:
    vertices_dict = {}

    for name in vertices:
        vertices_dict[name] = Vertex(name)

    return Graph(
        [
            vertices_dict[name]
            for name in vertices
        ],
        [
            Edge(
                "{} - {}".format(name1, name2),
                vertices_dict[name1],
                vertices_dict[name2]
            )
            for (name1, name2) in edges
        ]
    )