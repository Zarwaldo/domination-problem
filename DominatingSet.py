
from typing import List, Tuple, Dict
from Graph import Graph, buildGraph


def minimalDominatingSet(vertices : List[str], edges : List[Tuple[str]]) -> List[str]:
    def aux(graph : Graph):
        def aux2(graph : Graph, stack : List[str], result : List[str], explored_roots : Dict[str, bool]):
            unmarked_components = graph.getUnmarkedConnectedComponents()

            if len(unmarked_components) > 1:
                r = []

                for c in unmarked_components:
                    r += aux(c)

                if len(r) < len(result):
                    result.clear()
                    for v in r:
                        result.append(v)

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
                and v.getCoveringPotential() > 1
            ]

            remaining.sort(
                key = lambda v: -v.getCoveringPotential()
            )

            for name in [ v.getName() for v in remaining ]:
                graph_ = graph.copy()
                vertex = graph_.getVertexByName(name)
                vertex.cover()

                aux2(
                    graph_,
                    stack
                    + [ vertex.getName() ],
                    result,
                    explored_roots
                )

                if len(stack) == 0:
                    explored_roots[vertex.getName()] = True

                if len(stack) >= len(result) - 1:
                    return


        dominating : List[str] = [ v.getName() for v in graph.getVertices() ]
        aux2(graph, [], dominating, { v.getName(): False for v in graph.getVertices() })

        return dominating

    graph = buildGraph(vertices, edges)
    return aux(graph)
