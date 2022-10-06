
from typing import List, Tuple, Dict
from Graph import Graph, buildGraph


def minimalDominatingSet(vertices : List[str], edges : List[Tuple[str]]) -> List[str]:
    def stackToInt(graph : Graph, stack : List[str]):
        r = 0

        names = sorted([ v.getName() for v in graph.getVertices() ])
        for i in range(len(names)):
            if names[i] in stack:
                r += 2**i

        return r

    def aux(graph : Graph, stack : List[str], result : List[str], explored_subsets : List[int]):
        print(stack, end = '\r')
        if len(stack) >= len(result):
            return

        finished = True

        for v in graph.getVertices():
            if not v.isMarked():
                finished = False

        if finished:
            result.clear()
            for v in stack:
                result.append(v)

        if len(stack) >= len(result) - 1:
            return

        for i in range(2**len(stack)):
            subset = [ stack[j] for j in range(len(stack) - 1) if i & (2**j) == (2**j) ]
            if stackToInt(graph, subset) in explored_subsets:
                return

        lone_vertices = [
            v.getName()
            for v in graph.getVertices()
            if v.getCoveringPotential() == 1
            and not v.isMarked() 
        ]

        remaining = [
            v
            for v in (
                graph.getDisk([ graph.getVertexByName(name) for name in stack ], 3)
                if len(stack) > 0
                else graph.getVertices()
            )
            if v.getName() not in stack
            and v not in lone_vertices
        ]

        remaining.sort(
            key = lambda v: -v.getCoveringPotential()
        )

        for name in [ v.getName() for v in remaining ]:
            graph_ = graph.copy()
            vertex = graph_.getVertexByName(name)
            vertex.cover()

            aux(
                graph_,
                stack + [ vertex.getName() ],
                result,
                explored_subsets
            )

            explored_subsets.append(stackToInt(graph, stack + [ vertex.getName() ]))

            if len(stack) >= len(result) - 1:
                return


    graph = buildGraph(vertices, edges)
    components : List[Graph] = graph.getConnectedComponents()

    result : List[str] = []

    for component in components:
        dominating : List[str] = [ v.getName() for v in component.getVertices() ]
        aux(component, [], dominating, [])
        result += dominating

    return result
